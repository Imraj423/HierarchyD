def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
