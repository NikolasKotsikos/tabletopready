from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Miniature


def all_miniatures(request):
    """ A view to show all miniatures, including sorting and search queries """

    miniatures = Miniature.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('miniatures'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            miniatures = miniatures.filter(queries)

    context = {
        'miniatures': miniatures,
        'search_term': query,
    }

    return render(request, 'miniatures/miniatures.html', context)


def miniature_details(request, miniature_id):
    """ A view to show individual miniature details """

    miniature = get_object_or_404(Miniature, pk=miniature_id)

    context = {
        'miniature': miniature,
    }

    return render(request, 'miniatures/miniature_details.html', context)
