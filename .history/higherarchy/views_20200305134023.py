from django.shortcuts import render
from .models import FilesandFolders


def show_genres(request):
    paths = FilesandFolders.objects.get.all()
    return render(request, "home.html",
                  {'genres': FilesandFolders.objects.all()}
                  )
