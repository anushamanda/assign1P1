from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'places/places.html')
def place(request):
    return render(request, 'places/place.html')
def search(request):
    return render(request, 'places/search.html')

