from django import forms
from .models import Files


class FileForm(forms.Form):
    file_name = forms.CharField(label='File name', max_length=100)
    parent = forms.ModelChoiceField(queryset=Files.objects.all())
