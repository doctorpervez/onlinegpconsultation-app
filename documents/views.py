# documents/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document, DocumentCategory
from consultations.models import Patient
from .forms import DocumentForm

@login_required
def patient_documents(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    documents = Document.objects.filter(patient=patient)
    return render(request, 'documents/patient_documents.html', {
        'patient': patient,
        'documents': documents,
    })


@login_required
def upload_document(request, patient_id, consultation_id=None):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.patient = patient
            document.uploaded_by = request.user
            document.save()
            return redirect('documents:patient_documents', patient_id=patient_id)
    else:
        form = DocumentForm()
    return render(request, 'documents/upload_document.html', {
        'form': form,
        'patient': patient,
        'consultation_id': consultation_id,
    })

@login_required
def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    patient_id = document.patient.id
    document.delete()
    return redirect('documents:patient_documents', patient_id=patient_id)
