# prescriptions/views.py
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm
from .models import Prescription
from consultations.models import Consultation, Patient

@login_required
def add_prescription(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.consultation = consultation
            prescription.save()
            return redirect('consultations:consultation_detail', consultation_id)
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/add_prescription.html', {'form': form, 'consultation': consultation})

@login_required
def prescription_detail(request, id):
    prescription = get_object_or_404(Prescription, id=id)
    return render(request, 'prescriptions/prescription_detail.html', {'prescription': prescription })


@login_required
def print_prescriptions(request, patient_id):
    if request.method == 'POST':
        prescription_ids = request.POST.getlist('prescription_ids')
        prescriptions = Prescription.objects.filter(pk__in=prescription_ids)
        patient = get_object_or_404(Patient, pk=patient_id)
        return render(request, 'prescriptions/print_prescriptions.html', {'prescriptions': prescriptions, 'patient': patient})
    else:
        # If the request method is not POST, redirect to the patient's prescription list
        return redirect('patient_prescriptions', patient_id=patient_id)

# prescriptions/views.py (add this import)

# @login_required
# def print_prescription(request, id):
#     prescription = get_object_or_404(Prescription, id=id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="prescription_{prescription.id}.pdf"'

#     p = canvas.Canvas(response, pagesize=letter)
#     p.drawString(100, 750, f"Prescription for {prescription.consultation.patient}")
#     p.drawString(100, 735, f"Date: {prescription.date}")
#     p.drawString(100, 720, f"Medication: {prescription.medication}")
#     p.drawString(100, 705, f"Dosage: {prescription.dosage}")
#     p.drawString(100, 690, f"Instructions: {prescription.instructions}")
#     p.showPage()
#     p.save()

#     return response


@login_required
def patient_prescriptions(request, patient_id, consultation_id=None):
    patient = get_object_or_404(Patient, id=patient_id)
    prescriptions = Prescription.objects.filter(consultation__patient=patient).order_by('-date')
    return render(request, 'prescriptions/patient_prescriptions.html', {'patient': patient, 'prescriptions': prescriptions, 'consultation_id':consultation_id})
