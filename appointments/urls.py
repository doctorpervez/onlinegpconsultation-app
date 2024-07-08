from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.appointment_dashboard, name='appointment_dashboard'),
    path('list/', views.appointment_list, name='appointment_list'),
    path('<int:patient_id>/create/', views.create_appointment, name='create_appointment'),
    path('<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('<int:pk>/edit/', views.edit_appointment, name='edit_appointment'),
]
