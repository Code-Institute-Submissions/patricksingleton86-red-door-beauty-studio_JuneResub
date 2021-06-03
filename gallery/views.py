from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Style
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Style
from .forms import GalleryForm


# Create your views here.

def gallery(request):
    """ View to display some of the clients work, to show the quality & care involved """

    gallery = Style.objects.all()

    context = {
        'gallery': gallery,
    }
    
    return render(request, 'gallery/gallery.html', context)


@login_required
def add_picture(request):
    """ Add a service to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save()
            messages.success(request, 'Successfully added picture!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add picture. Please ensure the form is valid.')
    else:
        form = GalleryForm()

    template = 'gallery/add_picture.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_picture(request, style_id):
    """ Edit a picture in the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    gallery = get_object_or_404(Gallery, pk=style_id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=style)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated picture!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to update picture. Please ensure the form is valid.')
    else:
        form = GalleryForm(instance=style)
        messages.info(request, f'You are editing {style.name}')

    template = 'gallery/edit_picture.html'
    context = {
        'form': form,
        'style': style,
    }

    return render(request, template, context)


@login_required
def delete_picture(request, style_id):
    """ Delete a pictuure from the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    picture = get_object_or_404(Gallery, pk=style_id)
    picture.delete()
    messages.success(request, 'Picture deleted!')
    return redirect(reverse('gallery'))

