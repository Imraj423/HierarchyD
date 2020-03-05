
from django.shortcuts import render
from higherarchy.models import File


def show_files(request):
    html = 'home.html'

    files = File.objects.filter(user=request.user)
    return render(request, html, {
        'files': files,
        'user': request.user
    })
