from django.shortcuts import render
from .models import Film
# Create your views here.

def film_list(request):
    films=Film.objects.all()
    return render (request, "films/film_list.html", {'films':films})
