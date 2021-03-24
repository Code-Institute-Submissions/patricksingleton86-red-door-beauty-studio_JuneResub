from django.shortcuts import render, redirect, reverse
from .models import Service, Category
# Create your views here.

def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()
    categories = Category.objects.all()
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'services': services,
        'categories': categories,
        'current_categories': categories,
    }

    return render(request, 'services/services.html', context)
