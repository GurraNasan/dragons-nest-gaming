from django.urls import path
from . import views

app_name = "calender"
urlpatterns = [
    path('', views.calendar_view.as_view(), name="calendar"),
    path('event_info/<event_id>', views.event_info, name="event_info"),
    path('delete_event/<event_id>', views.delete_event, name="delete_event"),
    path('add_event/', views.event, name="add_event"),
    path('edit_event/<event_id>', views.event, name="edit_event"),
    
]
