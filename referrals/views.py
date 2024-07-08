# referrals/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.crypto import get_random_string
from .models import Referral
from .forms import ReferralForm
from consultations.models import Patient

@login_required(login_url='/')
def create_referral(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.patient = patient
            referral.referring_clinician = request.user
            referral.access_code = get_random_string(6)
            referral.save()
            return redirect('referrals:referral_detail', referral.pk)
    else:
        form = ReferralForm()
    return render(request, 'referrals/create_referral.html', {'form': form, 'patient': patient})


def referral_detail(request, pk):
    referral = get_object_or_404(Referral, pk=pk)
    return render(request, 'referrals/referral_detail.html', {'referral': referral})

def referral_access(request, access_code):
    try:
        referral = get_object_or_404(Referral, access_code=access_code)
        return render(request, 'referrals/referral_detail.html', {'referral': referral})
    except:
        messages.error(request, 'Invalid access code. Please try again.')
        return redirect('referrals:referral_access_page')

def referral_access_page(request):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        return redirect('referrals:referral_access', access_code=access_code)
    return render(request, 'referrals/referral_access_page.html')

@login_required(login_url='/')
def patient_referrals(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    referrals = Referral.objects.filter(patient=patient)
    return render(request, 'referrals/all_referrals.html', {'patient': patient, 'referrals': referrals})
