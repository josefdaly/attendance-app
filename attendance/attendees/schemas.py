from marshmallow import Schema, fields, post_load
from common.fields import DjangoModelID

from attendees.models import Attendee
from scheduling.models import RecurringScheduledSession


class AttendeeSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    session_date = fields.Date()
    recurring_scheduled_session = DjangoModelID(model=RecurringScheduledSession)

    @post_load
    def make_attendee(self, data, **kwargs):
        return Attendee(**data)
