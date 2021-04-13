from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from miniatures.models import Miniature 

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add ad quantity of the specified miniature to the shopping cart """

    miniature = Miniature.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    faction = None
    if 'miniature_faction' in request.POST:
        faction = request.POST['miniature_faction']
    cart = request.session.get('cart', {})

    if faction:
        if item_id in list(cart.keys()):
            if faction in cart[item_id]['items_by_faction'].keys():
                cart[item_id]['items_by_faction'][faction] += quantity
            else:
                cart[item_id]['items_by_faction'][faction] = quantity
        else:
            cart[item_id] = {'items_by_faction': {faction: quantity}}

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {miniature.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the quantity of specific"""
    """ miniature to the specified amount """

    quantity = int(request.POST.get('quantity'))
    faction = None
    if 'miniature_faction' in request.POST:
        faction = request.POST['miniature_faction']
    cart = request.session.get('cart', {})

    if faction:
        if quantity > 0:
            cart[item_id]['items_by_faction'][faction] = quantity
        else:
            del cart[item_id]['items_by_faction'][faction]
            if not cart[item_id]['items_by_faction']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """

    try:
        faction = None
        if 'miniature_faction' in request.POST:
            faction = request.POST['miniature_faction']
        cart = request.session.get('cart', {})

        if faction:
            del cart[item_id]['items_by_faction'][faction]
            if not cart[item_id]['items_by_faction']:
                cart.pop(item_id)

        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
