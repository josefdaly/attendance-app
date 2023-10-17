import datetime
import factories

from marshmallow import ValidationError
from django.test import TestCase

from attendees.schemas import AttendeeSchema


class AttendeeSchemaTestCase(TestCase):

    def test_loads_attendee_object(self):
        session = factories.RecurringScheduledSessionFactory()

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'session_date': '2023-10-15',
            'recurring_scheduled_session': session.pk
        }

        attendee = AttendeeSchema().load(data)
        attendee.save()
        self.assertEqual(attendee.first_name, 'John')
        self.assertEqual(attendee.last_name, 'Doe')
        self.assertEqual(attendee.session_date, datetime.date(2023, 10, 15))
        self.assertEqual(attendee.recurring_scheduled_session, session)
        self.assertIsNone(attendee.one_time_scheduled_session)

        one_time_session = factories.OneTimeScheduledSessionFactory()

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'session_date': '2023-10-15',
            'one_time_scheduled_session': one_time_session.pk
        }

        attendee = AttendeeSchema().load(data)
        attendee.save()
        self.assertEqual(attendee.first_name, 'John')
        self.assertEqual(attendee.last_name, 'Doe')
        self.assertEqual(attendee.session_date, datetime.date(2023, 10, 15))
        self.assertIsNone(attendee.recurring_scheduled_session)
        self.assertEqual(attendee.one_time_scheduled_session, one_time_session)

    def test_schema_validation(self):
        recurring_session = factories.RecurringScheduledSessionFactory()
        one_time_session = factories.OneTimeScheduledSessionFactory()

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'session_date': '2023-10-15',
            'recurring_scheduled_session': recurring_session.pk,
            'one_time_scheduled_session': one_time_session.pk,
        }

        with self.assertRaises(ValidationError):
            AttendeeSchema().load(data)

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'session_date': '2023-10-15',
        }

        with self.assertRaises(ValidationError):
            AttendeeSchema().load(data)
