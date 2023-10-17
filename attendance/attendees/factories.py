import factory, datetime

from attendees.models import Attendee


class AttendeeFactory(factory.DjangoModelFactory):

    class Meta:
        model = Attendee

    first_name = 'John'
    last_name = 'Doe'
    session_date = datetime.date.today()
    recurring_scheduled_session = factory.SubFactory('scheduling.factories.RecurringScheduledSessionFactory')
