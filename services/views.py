from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Service, Treatment
from .forms import ServiceForm
# Create your views here.

def all_services(request):
    """ A view to show all services """

    services = Service.objects.all()
    treatments = Treatment.objects.all()
    treatments = None

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


@login_required
def add_service(request):
    """ Add a service to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Product, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete a service from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=product_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))

