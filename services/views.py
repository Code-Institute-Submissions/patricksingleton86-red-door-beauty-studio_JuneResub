from django.shortcuts import render
from .models import Service, Category
# Create your views here.

def all_services(request):
    """ A view to show all services """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'services/services.html', context)
