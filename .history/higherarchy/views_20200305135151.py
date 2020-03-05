from django.shortcuts import render
from .models import Files


def show_genres(request):
    paths = Files.objects.get.all()
    return render(request, "home.html",
                  {'genres': Files.objects.all()}
                  )
