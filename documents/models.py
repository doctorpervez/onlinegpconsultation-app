from django.db import models
from accounts.models import CustomUser
from consultations.models import Patient



class DocumentCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



