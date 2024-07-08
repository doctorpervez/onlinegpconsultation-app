from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from consultations.models import Patient
from django.utils import timezone
from datetime import timedelta

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(clinician=request.user)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def create_appointment(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create_appointment.html', {'form': form, 'patient': patient})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_dashboard')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form})



def appointment_dashboard(request):
    # Get the current date and time
    now = timezone.now()

    # Determine the filter based on the selected view
    view = request.GET.get('view', 'day')  # default to 'day'
    
    if view == 'day':
        start_date = now.replace(hour=0, minute=0, second=0)
        end_date = now.replace(hour=23, minute=59, second=59)
    elif view == 'week':
        start_date = now - timedelta(days=now.weekday())  # Start of the week
        end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59)  # End of the week
    elif view == 'month':
        start_date = now.replace(day=1, hour=0, minute=0, second=0)
        next_month = start_date.replace(day=28) + timedelta(days=4)  # this will never fail
        end_date = (next_month - timedelta(days=next_month.day)).replace(hour=23, minute=59, second=59)  # End of the month
    else:
        start_date = now.replace(hour=0, minute=0, second=0)
        end_date = now.replace(hour=23, minute=59, second=59)
    
    # Filter the appointments based on the selected view
    appointments = Appointment.objects.filter(date__range=[start_date, end_date])
    clinicians = Appointment.objects.values_list('clinician__username', flat=True).distinct()

    return render(request, 'appointments/appointment_dashboard.html', {
        'appointments': appointments,
        'view': view,
        'clinicians': clinicians,
    })
