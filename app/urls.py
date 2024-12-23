from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Added a name for the route
]
