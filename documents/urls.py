# documents/urls.py
from django.urls import path
from . import views

app_name = 'documents'
urlpatterns = [
    path('patient/<int:patient_id>/documents/', views.patient_documents, name='patient_documents'),
    path('patient/<int:patient_id>/documents/upload/', views.upload_document, name='upload_document'),
    path('patient/<int:patient_id>/documents/upload/back_to_cons_detail/<int:consultation_id>/', views.upload_document, name='upload_document_redirection_from_cons'),
    path('document/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]
