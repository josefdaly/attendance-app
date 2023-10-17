import datetime
from dateutil import parser

from django.shortcuts import render
from django.views.generic import View
from django.core import serializers

from common.render import json_response
from scheduling.models import RecurringScheduledSession, OneTimeScheduledSession
from scheduling.schemas import RecurringScheduledSessionSchema, OneTimeScheduledSessionSchema
from scheduling import constants


class OneWeekScheduleView(View):

    def get(self, request, configuration_id):
        recurring_sessions = RecurringScheduledSession.objects.filter(schedule_config_id=configuration_id).prefetch_related('attendees')
        one_time_scheduled_sessions = OneTimeScheduledSession.objects.filter(
            schedule_config_id=configuration_id,
            date__gte=datetime.date.today(),
            date__lte=datetime.date.today() + datetime.timedelta(days=7),
        ).prefetch_related('attendees')
        session_list = RecurringScheduledSessionSchema(many=True).dump(recurring_sessions) + OneTimeScheduledSessionSchema(many=True).dump(one_time_scheduled_sessions)
        session_list.sort(key=lambda x: parser.parse(x['date']))
        return json_response(session_list)
