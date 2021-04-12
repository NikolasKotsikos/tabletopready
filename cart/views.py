from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add ad quantity of the specified miniature to the shopping cart """

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

    request.session['cart'] = cart
    return redirect(redirect_url)
