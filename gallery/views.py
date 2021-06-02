from django.shortcuts import render
from .models import Style

# Create your views here.

def gallery(request):
    """ View to display some of the clients work, to show the quality & care involved """

    gallery = Style.objects.all()

    context = {
        'gallery': gallery,
    }
    
    return render(request, 'gallery/gallery.html', context)