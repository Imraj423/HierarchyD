from higherarchy.forms import FileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from higherarchy.models import File


def show_files(request):
    return render(request, "home.html", {'files': File.objects.all()})


def add_files(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                file_name=data['file_name'],
                parent=data["parent"]
            )
            return HttpResponseRedirect('/')
    else:
        form = FileForm()
    return render(request, "addfile.html", {'form': form})
