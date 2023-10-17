from django.db import models

from scheduling import constants


class ScheduleConfiguration(models.Model):
    name = models.CharField(max_length=255)


class RecurringScheduledSession(models.Model):
    name = models.CharField(max_length=255)
    day = models.IntegerField(choices=constants.DAY_OF_THE_WEEK_CHOICES)
    time = models.TimeField()
    schedule_config = models.ForeignKey(ScheduleConfiguration, on_delete=models.CASCADE)

    @property
    def type(self):
        return 'recurring'


class OneTimeScheduledSession(models.Model):
    name = models.CharField(max_length=255)
    time = models.TimeField()
    schedule_config = models.ForeignKey(ScheduleConfiguration, on_delete=models.CASCADE)
    date = models.DateField()

    @property
    def type(self):
        return 'one-time'
