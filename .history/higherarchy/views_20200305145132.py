
from django.shortcuts import render, HttpResponseRedirect, reverse
from higherarchy.models import File
from .forms import AddFileForm, NewUserForm, LoginForm


def show_files(request):
    html = 'home.html'

    files = File.objects.filter(user=request.user)
    return render(request, html, {
        'files': files
    })


def new_file_view(request):
    html = 'generic_form.html'
    if request.method == 'POST':
        form = AddFileForm(request.user, request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                folder=data['folder'],
                parent=data['parent'],
                user=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddFileForm(request.user)
    return render(request, html, {'form': form})
