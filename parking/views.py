from django.shortcuts import render
from .models import Parking

def map_view(request):
    parkings = Parking.objects.all()
    return render(request, 'map.html', {'parkings': parkings})