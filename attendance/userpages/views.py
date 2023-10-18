import datetime, json
from dateutil import parser

from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from django.core import serializers

from attendees.schemas import AttendeeSchema
from common.render import json_response
from scheduling.models import RecurringScheduledSession, OneTimeScheduledSession
from scheduling.schemas import RecurringScheduledSessionSchema, OneTimeScheduledSessionSchema
from scheduling import constants


class ScheduleListView(View):

    def get(self, request, configuration_id):
        recurring_sessions = RecurringScheduledSession.objects.filter(schedule_config_id=configuration_id).prefetch_related('attendees')
        one_time_scheduled_sessions = OneTimeScheduledSession.objects.filter(
            schedule_config_id=configuration_id,
            date__gte=datetime.date.today(),
            date__lte=datetime.date.today() + datetime.timedelta(days=7),
        ).prefetch_related('attendees')
        session_list = RecurringScheduledSessionSchema(many=True).dump(recurring_sessions) + OneTimeScheduledSessionSchema(many=True).dump(one_time_scheduled_sessions)
        session_list.sort(key=lambda x: parser.parse(x['date']))

        template = loader.get_template("userpages/schedules.html")

        return HttpResponse(template.render({'sessions': session_list}, request))


class ScheduleDetailView(View):

    def _get_session_data(self, session_id, session_type):
        session_cls = None
        session_serializer = None
        if session_type == 'recurring_scheduled_session':
            session_cls = RecurringScheduledSession
            session_serializer = RecurringScheduledSessionSchema
        elif session_type == 'one_time_scheduled_session':
            session_cls = OneTimeScheduledSession
            session_serializer = OneTimeScheduledSessionSchema
        else:
            raise Exception('everything is fucked')

        session = session_cls.objects.get(pk=session_id)
        return session_serializer().dump(session)

    def get(self, request, session_id, session_type):
        session_data = self._get_session_data(session_id, session_type)

        template = loader.get_template("userpages/session-detail.html")

        return HttpResponse(template.render({'session': session_data}, request))

    def post(self, request, session_id, session_type):
        data = json.loads(json.dumps(request.POST))
        data.pop('csrfmiddlewaretoken')
        attendee = AttendeeSchema().load(data)
        attendee.save()
        session_data = self._get_session_data(session_id, session_type)

        template = loader.get_template("userpages/session-detail.html")

        return HttpResponse(template.render({'session': session_data}, request))
