from django.urls import path
from . import views

urlpatterns = [
    path('', views.calender.as_view(), name="calender"),
]
