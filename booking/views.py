from django.shortcuts import render

# Create your views here.

def booking(request):
    """ View to return to index page """
    
    return render(request, 'booking/booking.html')