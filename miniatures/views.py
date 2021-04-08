from django.shortcuts import render, get_object_or_404
from .models import Miniature


def all_miniatures(request):
    """ A view to show all miniatures, including sorting and search queries """

    miniatures = Miniature.objects.all()

    context = {
        'miniatures': miniatures,
    }

    return render(request, 'miniatures/miniatures.html', context)


def miniature_details(request, miniature_id):
    """ A view to show individual miniature details """

    miniature = get_object_or_404(Miniature, pk=miniature_id)

    context = {
        'miniature': miniature,
    }

    return render(request, 'miniatures/miniature_details.html', context)
