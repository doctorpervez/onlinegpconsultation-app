from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100, null=True, blank=True )
    phone = models.CharField(max_length=20, null=True, blank=True )
    next_of_kin = models.CharField(max_length=100, null=True, blank=True )
    next_of_kin_phone = models.CharField(max_length=20, null=True, blank=True )



    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return f"Consultation on {self.date} for {self.patient}"
    

class TestChoice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Test(models.Model):
    consultation = models.ForeignKey('Consultation', related_name='tests', on_delete=models.CASCADE)
    test_choice = models.ForeignKey(TestChoice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.test_choice.name} for {self.consultation}"
