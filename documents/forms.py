from django import forms
from .models import Document, DocumentCategory

class DocumentForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=DocumentCategory.objects.all(), required=False)

    class Meta:
        model = Document
        fields = ['title', 'file', 'category']

        widgets = {
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'file': forms.ClearableFileInput(attrs={'class':'form-control'}),
                'category': forms.Select(attrs={'class':'form-control'}),


            }