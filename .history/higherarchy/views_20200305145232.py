
from mptt.admin import MPTTModelAdmin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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


def register_user_view(request):
    html = 'generic_form.html'
    page = 'register'
    if request.method == "POST":

        form = NewUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = NewUserForm()

    return render(request, html, {'form': form, 'page': page})


def login_view(request):
    html = 'generic_form.html'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home'))
            )
    form = LoginForm()
    return render(request, html, {'form': form, 'page': page})
