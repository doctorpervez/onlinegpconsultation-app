# referrals/models.py
from django.db import models
from django.utils.crypto import get_random_string
from consultations.models import Patient
from accounts.models import CustomUser

class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referring_clinician = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='referrals_made')
    referred_to_clinician = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200)
    reason = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    access_code = models.CharField(max_length=6, unique=True, default=get_random_string(6))
