from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse
from higherarchy.models import File
from .forms import AddFileForm, NewUserForm, LoginForm


def show_files(request):
    html = 'home.html'

    files = File.objects.filter(user=request.user)
    return render(request, html, {
        'files': files
    })
