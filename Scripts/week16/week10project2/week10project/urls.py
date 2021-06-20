from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu409123456', views.ccu409123456_function)
]

