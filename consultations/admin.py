from django.contrib import admin
from .models import Patient, Consultation, Test, TestChoice
# Register your models here.

admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(TestChoice)
admin.site.register(Test)



