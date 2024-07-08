from django.shortcuts import render, redirect, get_object_or_404
from .models import Consultation, Patient, Test
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .forms import ConsultationForm, TestForm
from django.db.models import Q
from prescriptions.models import Prescription
from prescriptions.forms import PrescriptionForm

@login_required
def consultation_list(request):
    consultations = Consultation.objects.all()
    return render(request, 'consultations/consultation_list.html', {'consultations': consultations})

@login_required
def consultation_detail(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    prescriptions = Prescription.objects.filter(consultation=consultation).order_by('-date')
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.consultation = consultation
            prescription.save()
            return redirect('consultations:consultation_detail', consultation_id=consultation_id)
    else:
        form = PrescriptionForm()
    return render(request, 'consultations/consultation_detail.html', {'consultation': consultation, 'prescriptions': prescriptions, 'form':form,})

@login_required
def consultation_add(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')
    else:
        form = ConsultationForm()
    return render(request, 'consultations/consultation_add.html', {'form': form})
# Create your views here.


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'consultations/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    consultations = Consultation.objects.filter(patient=patient).order_by('-date')
  
    
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = patient
            consultation.save()
            return redirect('consultations:patient_detail', pk=patient.pk)
    else:
        form = ConsultationForm()
    
    return render(request, 'consultations/patient_detail.html', {
        'patient': patient,
        'consultations': consultations,
        'form': form,
    })


def search_patient(request):
    query = request.GET.get('q')
    patients = None
    if query:
        patients = Patient.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(phone__icontains=query)) # Adjust the filter as needed
    return render(request, 'consultations/search_patient.html', {'patients': patients, 'query': query})

@login_required(login_url='/')
def add_tests(request, consultation_id):
    consultation = get_object_or_404(Consultation, pk=consultation_id)
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            tests = form.cleaned_data['test_choices']
            for test_choice in tests:
                Test.objects.create(consultation=consultation, test_choice=test_choice)

            return redirect('consultations:consultation_detail', consultation_id)
    else:
        form = TestForm()
    return render(request, 'consultations/add_tests.html', {'form': form, 'consultation': consultation})

@login_required(login_url='/')
def print_tests(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    tests = Test.objects.filter(consultation=consultation)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="tests_for_{consultation.patient}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Draw the title
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 40, f"Tests for {consultation.patient}")
    # draw pt details
    p.setFont("Helvetica", 12)
    y = height - 60
    p.drawString(100, y, f"DOB: {consultation.patient.date_of_birth}, Diagnosis:{consultation.diagnosis}")
    y -= 80
    # Draw the test details
    p.setFont("Helvetica", 12)
    y = height - 80
    for test in tests:
        p.drawString(100, y, f"- {test.test_choice.name}")
        y -= 20

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    return response