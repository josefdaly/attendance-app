import factory, datetime

from scheduling.models import ScheduleConfiguration, RecurringScheduledSession, OneTimeScheduledSession
from scheduling import constants


class ScheduleConfigurationFactory(factory.DjangoModelFactory):

    class Meta:
        model = ScheduleConfiguration

    name = 'Configuration'


class RecurringScheduledSessionFactory(factory.DjangoModelFactory):

    class Meta:
        model = RecurringScheduledSession

    name = 'Training Session'
    day = constants.MONDAY
    time = datetime.datetime.now().time()
    schedule_config = factory.SubFactory(ScheduleConfigurationFactory)


class OneTimeScheduledSessionFactory(factory.DjangoModelFactory):

    class Meta:
        model = OneTimeScheduledSession

    name = 'Special Training Session'
    time = datetime.datetime.now().time()
    schedule_config = factory.SubFactory(ScheduleConfigurationFactory)
    date = datetime.date.today()
