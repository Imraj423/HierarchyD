from django.shortcuts import render
from higherarchy.models import File


def show_files(request):
    html = 'home.html'

    files = File.objects.all()
    return render(request, html, {
        'files': files
    })
