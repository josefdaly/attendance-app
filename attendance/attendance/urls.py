"""
URL configuration for attendance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from scheduling import views as schedule_views
from attendees import views as attendee_views
from userpages import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # API Views
    path('api/schedules/<configuration_id>/', schedule_views.OneWeekScheduleView.as_view(), name='schedules'),
    path('api/attendees/', attendee_views.AttendeeView.as_view(), name='attendees'),
    # User Application Views
    path('schedules/<configuration_id>/', user_views.ScheduleListView.as_view()),
    path('schedules/<configuration_id>/sessions/<session_id>/<session_type>/', user_views.ScheduleDetailView.as_view()),
]
