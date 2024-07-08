# prescriptions/urls.py
from django.urls import path
from . import views

app_name = 'prescriptions'

urlpatterns = [
    path('add/<int:consultation_id>/', views.add_prescription, name='add_prescription'),
    path('<int:id>/', views.prescription_detail, name='prescription_detail'),
    path('print/<int:patient_id>/', views.print_prescriptions, name='print_prescriptions'),
    path('patient_all_px/<int:patient_id>/', views.patient_prescriptions, name='patient_prescriptions'),
    path('patient_all_px/<int:patient_id>/redirection_from_cons/<int:consultation_id>/', views.patient_prescriptions, name='patient_prescriptions_redirection_from_cons'),

]
