from django.urls import path
from w16project import views

urlpatterns = [
    path('', views.home),
]