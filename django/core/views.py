from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from core.models import Movie

class MovieList(ListView):

    # ListView requires atleast a model attribute, Hence added the same below.
    # It will query for all the rows of that model, pass it to the template
    # and returned the rendered template in a response.
    model = Movie
    paginate_by = 2

class MovieDetail(DetailView):
    model = Movie
