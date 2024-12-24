from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Added a name for the route
    path('update/<str:pk>/', views.update, name='update_task'),
    path('delete/<str:pk>/', views.delete, name='delete'),

]
