from django.shortcuts import render, redirect, reverse
from services.models import Service, Treatment

# Create your views here.

def booking(request):
    """ View to return to index page """

    return render(request, 'booking/booking.html')
