from django.contrib.auth.models import User
from .models import File
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class AddFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'parent', 'folder']

    def __init__(self, user, * args, **kwargs):
        super(AddFileForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = File.objects.filter(
            folder=True, user=user
        )
