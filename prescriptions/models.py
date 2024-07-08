# prescriptions/models.py
from django.db import models
from consultations.models import Consultation

class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='prescriptions')
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.consultation.patient} on {self.date}"
    
   

    
