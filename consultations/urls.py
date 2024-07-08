from django.urls import path
from . import views

app_name = 'consultations'

urlpatterns = [
    path('', views.consultation_list, name='consultation_list'),
    path('patient_list/', views.patient_list, name='patient_list'),
    path('search/', views.search_patient, name='search_patient'),
    path('patient_detail/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('add/', views.consultation_add, name='consultation_add'),
    path('<int:consultation_id>/', views.consultation_detail, name='consultation_detail'),
    path('consultation/<int:consultation_id>/add_tests/', views.add_tests, name='add_tests'),
    path('consultation/<int:consultation_id>/print_tests/', views.print_tests, name='print_tests'),
]