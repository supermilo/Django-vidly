from platform import release
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.

def  index(request):
    # x = 1
    # y = 2
    # Movie.objects.all()
    # Movie.objects.filter(release_year=1984)
    # Movie.objects.get(id=1)
    movies = Movie.objects.all()
    #type(movies)
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    # return render(request, 'hello.html', { 'names':'bunny'})
    # return render(request, 'hello.html', { 'name':'bunny'})
    return render(request, 'movies/index.html', {'movieses': movies })

def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     # Movie.objects.get(id=movie_id) , es igual q el anterior primary key = pk
    #     # return HttpResponse(movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie })
    # except Movie.DoesNotExist:
    #     raise Http404()
    # we now pass the model for the next function as first parameter
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie })

