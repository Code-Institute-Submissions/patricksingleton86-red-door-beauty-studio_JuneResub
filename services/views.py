from django.shortcuts import render, redirect, reverse
from .models import Service, Treatment
# Create your views here.

def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()
    treatments = Treatment.objects.all()
    treatment = None

    if request.GET:
        if 'treatment' in request.GET:
            treatments = request.GET['treatment'].split(',')
            services = services.filter(treatment__name__in=treatments)
            treatments = Treatment.objects.filter(name__in=treatments)

    context = {
        'services': services,
        'treatments': treatments,
        'current_treatments': treatments,
    }

    return render(request, 'services/services.html', context)
