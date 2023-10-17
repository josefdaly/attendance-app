from django.db import models


class Attendee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    session_date = models.DateField(null=True)
    recurring_scheduled_session = models.ForeignKey('scheduling.RecurringScheduledSession', related_name='attendees', null=True, blank=True, on_delete=models.CASCADE)
    one_time_scheduled_session = models.ForeignKey('scheduling.OneTimeScheduledSession', related_name='attendees', null=True, blank=True, on_delete=models.CASCADE)
