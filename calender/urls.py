from django.urls import path
from . import views

app_name = "calender"
urlpatterns = [
    path('', views.calendar_view.as_view(), name="calendar"),
    path('add_event/', views.event, name="add_event"),
    path('edit_event/<event_id>', views.event, name="edit_event"),
]
