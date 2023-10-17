from django.shortcuts import render
from django.views.generic import View
from marshmallow import ValidationError

from attendees.schemas import AttendeeSchema
from common.render import json_response


class AttendeeView(View):

    def post(self, request):
        try:
            attendee = AttendeeSchema().loads(request.body)
        except ValidationError:
            return json_response({'error': 'ValidationError'}, status=400)
        attendee.save()
        return json_response({'attendee': AttendeeSchema().dump(attendee)})
