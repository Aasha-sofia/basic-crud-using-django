from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_registration, name='create_registration'),
    path('', views.read_registrations, name='read_registrations'),
    path('update/<str:reg_id>/', views.update_registration, name='update_registration'),
    path('delete/<str:reg_id>/', views.delete_registration, name='delete_registration'),
]
