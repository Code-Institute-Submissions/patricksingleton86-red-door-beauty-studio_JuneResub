from django.shortcuts import render
from .models import Booking

# Create your views here.

def booking(request):
    booking = Booking.objects.all()
    context = {
        'booking': booking
    }


    return render(request, 'booking/booking.html', context)
