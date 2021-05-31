from django.shortcuts import render
from .models import Booking

# Create your views here.

def booking(request):
    booking = Booking.objects.all()
    context = {
        'booking': booking
    }
    return render(request, 'booking/booking.html', context)

# def add_booking(request):
#     if request.method == 'POST':
#         name = request.POST.get()
#         treatment =
#         slot =
#         Booking.objects.create(name=name,)

#     return render(request, 'booking/add_booking.html')

