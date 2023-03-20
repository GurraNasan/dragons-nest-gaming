from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('privacy/', views.privacy, name="privacy"),
    path('return_and_refund/', views.return_and_refund, name="return_and_refund"),
    path('terms', views.terms, name="terms"),
]
