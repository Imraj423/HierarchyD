from django.shortcuts
def show_genres(request):
    return render(request, "home.html", {'genres': Genre.objects.all()})
