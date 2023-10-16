from django.contrib import admin

from scheduling.models import ScheduleConfiguration, RecurringScheduledSession, OneTimeScheduledSession

# Register your models here.

admin.site.register(ScheduleConfiguration)
admin.site.register(RecurringScheduledSession)
admin.site.register(OneTimeScheduledSession)
