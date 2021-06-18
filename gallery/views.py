from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GalleryItemForm
from .models import GalleryItem


def all_gallery_items(request):
    """ A view to show all gallery items """

    gallery_items = GalleryItem.objects.all()
    template = 'gallery/gallery.html'

    context = {
        'gallery_items': gallery_items,
    }

    return render(request, template, context)


@login_required
def add_gallery_item(request):
    """ Add an item to the gallery """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Successfully added item to the gallery!')
            return redirect(reverse('all_gallery_items'))
        else:
            messages.error(request,
                           'Failed to add item.'
                           'Please check that the form is valid.')
    else:
        form = GalleryItemForm()

    template = 'gallery/add_gallery_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gallery_item(request, gallery_item_id):
    """" Edit an army in the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    gallery_item = get_object_or_404(GalleryItem, pk=gallery_item_id)
    if request.method == 'POST':
        form = GalleryItemForm(request.POST,
                               request.FILES,
                               instance=gallery_item)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Successfully updated {gallery_item.name}')
            return redirect(
                            reverse('all_gallery_items'))
        else:
            messages.error(request,
                           f'Failed to update {gallery_item.name}.'
                           'Please check that the form is valid.')
    else:
        form = GalleryItemForm(instance=gallery_item)
        messages.info(request, f'You are editing {gallery_item.name}.')

    template = 'gallery/edit_gallery_item.html'
    context = {
        'form': form,
        'gallery_item': gallery_item,
    }

    return render(request, template, context)


@login_required
def delete_gallery_item(request, gallery_item_id):
    """ Deletes an item from the gallery """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    gallery_item = get_object_or_404(GalleryItem, pk=gallery_item_id)
    gallery_item.delete()
    messages.success(request, 'Gallery Item deleted!')
    return redirect(reverse('all_gallery_items'))
