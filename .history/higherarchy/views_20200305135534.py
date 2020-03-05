from .forms import FileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Files


def add_file(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Files.objects.create(
                file_name=data['file_name'],
                parent=data["parent"]
            )
            return HttpResponseRedirect('/')
    else:
        form = FileForm()

    return render(request, "home.html", {'form': form})
