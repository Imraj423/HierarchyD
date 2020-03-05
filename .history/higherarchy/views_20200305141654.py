
from django.shortcuts import render
from higherarchy.models import File


def show_files(request):
    return render(request, "home.html", {'file': File.objects.all()})
