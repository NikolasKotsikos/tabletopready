from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from miniatures.models import Miniature


def cart_contents(request):

    cart_items = []
    total = 0
    miniatures_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        miniature = get_object_or_404(Miniature, pk=item_id)
        total += quantity * miniature.price
        miniatures_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'miniature': miniature,
        })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'miniatures_count': miniatures_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
