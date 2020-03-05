from django.shortcuts import render
from .models import FilesandFolders


def show_genres(request):
    return render(request, "home.html",
    {'genres': FilesandFolders.objects.all()})
