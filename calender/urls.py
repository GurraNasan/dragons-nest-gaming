from django.urls import path
from . import views

app_name = "calender"
urlpatterns = [
    path('', views.calendar_view.as_view(), name="calendar"),
]
