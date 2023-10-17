import factory, datetime

from scheduling.models import ScheduleConfiguration, RecurringScheduledSession
from scheduling import constants


class ScheduleConfigurationFactory(factory.DjangoModelFactory):

    class Meta():
        model = ScheduleConfiguration

    name = 'Configuration'


class RecurringScheduledSessionFactory(factory.DjangoModelFactory):

    class Meta():
        model = RecurringScheduledSession

    name = 'Training Session'
    day = constants.MONDAY
    time = datetime.datetime.now()
    schedule_config = factory.SubFactory(ScheduleConfigurationFactory)
