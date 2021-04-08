from django.shortcuts import render
from .models import Miniature


def all_miniatures(request):
    """ A view to show all miniatures, including sorting and search queries """

    miniatures = Miniature.objects.all()

    context = {
        'miniatures': miniatures,
    }

    return render(request, 'miniatures/miniatures.html', context)
