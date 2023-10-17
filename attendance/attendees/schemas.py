from marshmallow import Schema, fields, post_load, validates_schema, ValidationError
from common.fields import DjangoModelID

from attendees.models import Attendee
from scheduling.models import RecurringScheduledSession, OneTimeScheduledSession


class AttendeeSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    session_date = fields.Date()
    recurring_scheduled_session = DjangoModelID(model=RecurringScheduledSession)
    one_time_scheduled_session = DjangoModelID(model=OneTimeScheduledSession)

    @validates_schema
    def ensure_exactly_one_session_relation(self, data, **kwargs):
        recurring_scheduled_session = data.get('recurring_scheduled_session')
        one_time_scheduled_session = data.get('one_time_scheduled_session')
        if not recurring_scheduled_session and not one_time_scheduled_session:
            raise ValidationError('At least one session relation must be specified')
        if recurring_scheduled_session and one_time_scheduled_session:
            raise ValidationError('Two session relations cannot be specified')

    @post_load
    def make_attendee(self, data, **kwargs):
        return Attendee(**data)
