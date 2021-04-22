from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.utils.html import strip_tags

from miniatures.models import Miniature


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add ad quantity of the specified miniature to the shopping cart """
    miniature = get_object_or_404(Miniature, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    faction = None

    if 'miniature_faction' in request.POST:
        faction = strip_tags(request.POST['miniature_faction'])
    cart = request.session.get('cart', {})

    if faction:
        if item_id in list(cart.keys()):
            if faction in cart[item_id]['items_by_faction'].keys():
                cart[item_id]['items_by_faction'][faction] += quantity
                messages.success(request,
                                 f'Updated {faction} {miniature.name} quantity to {cart[item_id]["items_by_faction"][faction]}'
                                 )
            else:
                cart[item_id]['items_by_faction'][faction] = quantity
                messages.success(
                    request, f'Added {faction} {miniature.name} to your cart')
        else:
            cart[item_id] = {'items_by_faction': {faction: quantity}}
            messages.success(
                request, f'Added {faction} {miniature.name} to your cart')

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             f'Updated {miniature.name} quantity to {cart[item_id]}'
                             )
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {miniature.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of specific"""
    """ miniature to the specified amount """

    miniature = get_object_or_404(Miniature, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    faction = None
    if 'miniature_faction' in request.POST:
        faction = strip_tags(request.POST['miniature_faction'])
    cart = request.session.get('cart', {})

    if faction:
        if quantity > 0:
            cart[item_id]['items_by_faction'][faction] = quantity
            messages.success(request,
                             f'Updated {faction} {miniature.name} quantity to {cart[item_id]["items_by_faction"][faction]}'
                             )
        else:
            del cart[item_id]['items_by_faction'][faction]
            if not cart[item_id]['items_by_faction']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed {faction} {miniature.name} from your cart')

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request,
                             f'Updated {miniature.name} quantity to {cart[item_id]}'
                             )
        else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {miniature.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        miniature = get_object_or_404(Miniature, pk=item_id)
        faction = None
        if 'miniature_faction' in request.POST:
            faction = strip_tags(request.POST['miniature_faction'])
        cart = request.session.get('cart', {})

        if faction:
            del cart[item_id]['items_by_faction'][faction]
            if not cart[item_id]['items_by_faction']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed {faction} {miniature.name} from your cart')

        else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {miniature.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
