from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from miniatures.models import Miniature


def cart_contents(request):

    cart_items = []
    total = 0
    miniature_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            miniature = get_object_or_404(Miniature, pk=item_id)
            total += item_data * miniature.price
            miniature_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'miniature': miniature,
            })
        else:
            miniature = get_object_or_404(Miniature, pk=item_id)
            for faction, quantity in item_data['items_by_faction'].items():
                total += quantity * miniature.price
                miniature_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'miniature': miniature,
                    'faction': faction,
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
        'miniature_count': miniature_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
