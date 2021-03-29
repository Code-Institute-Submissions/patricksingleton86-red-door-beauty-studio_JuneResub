from django.shortcuts import render

# Create your views here.

def bookings(request):
    """ View to return to index page """
    
    return render(request, 'bookings/bookings.html')