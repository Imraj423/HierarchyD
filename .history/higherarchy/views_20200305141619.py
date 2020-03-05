from higherarchy.forms import FileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from higherarchy.models import File


def show_files(request):
    return render(request, "home.html", {'files': File.objects.all()})
