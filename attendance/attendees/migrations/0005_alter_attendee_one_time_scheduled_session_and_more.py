# Generated by Django 4.2.6 on 2023-10-17 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_onetimescheduledsession'),
        ('attendees', '0004_attendee_one_time_scheduled_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='one_time_scheduled_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='scheduling.onetimescheduledsession'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='recurring_scheduled_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='scheduling.recurringscheduledsession'),
        ),
    ]
