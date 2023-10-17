import datetime
import factories

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
