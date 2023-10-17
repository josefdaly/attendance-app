from django.test import TestCase

import factories

from scheduling.schemas import RecurringScheduledSessionSchema, OneTimeScheduledSessionSchema


class RecurringScheduledSessionSchemaTestCase(TestCase):

    def setUp(self):
        self.recurring_session = factories.RecurringScheduledSessionFactory()
        self.attendee_1 = factories.AttendeeFactory(
            recurring_scheduled_session=self.recurring_session,
            one_time_scheduled_session=None
        )
        self.attendee_2 = factories.AttendeeFactory(
            recurring_scheduled_session=self.recurring_session,
            one_time_scheduled_session=None
        )

    def test_serialization(self):
        schema = RecurringScheduledSessionSchema()
        data = schema.dump(self.recurring_session)
        self.assertCountEqual(
            [attendee['id'] for attendee in data['attendees']],
            [self.attendee_1.pk, self.attendee_2.pk]
        )


class OneTimeScheduledSessionSchemaTestCase(TestCase):

    def setUp(self):
        self.one_time_session = factories.OneTimeScheduledSessionFactory()
        self.attendee_1 = factories.AttendeeFactory(
            one_time_scheduled_session=self.one_time_session,
            recurring_scheduled_session=None
        )
        self.attendee_2 = factories.AttendeeFactory(
            one_time_scheduled_session=self.one_time_session,
            recurring_scheduled_session=None
        )

    def test_serialization(self):
        schema = OneTimeScheduledSessionSchema()
        data = schema.dump(self.one_time_session)
        self.assertCountEqual(
            [attendee['id'] for attendee in data['attendees']],
            [self.attendee_1.pk, self.attendee_2.pk]
        )
