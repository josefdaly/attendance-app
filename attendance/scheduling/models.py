from django.db import models

from scheduling import constants


class ScheduleConfiguration(models.Model):
    name = models.CharField(max_length=255)


class RecurringScheduledSession(models.Model):
    name = models.CharField(max_length=255)
    day = models.IntegerField(choices=constants.DAY_OF_THE_WEEK_CHOICES)
    time = models.TimeField()
    schedule_config = models.ForeignKey(ScheduleConfiguration, on_delete=models.CASCADE)

    def __str__(self):
        return '{} at {}'.format(self.get_day_display(), self.time)

    @property
    def type(self):
        return 'recurring_scheduled_session'


class OneTimeScheduledSession(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    schedule_config = models.ForeignKey(ScheduleConfiguration, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return '{} at {}'.format(self.date, self.time)

    @property
    def type(self):
        return 'one_time_scheduled_session'
