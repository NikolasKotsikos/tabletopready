from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Miniature, GamingSystem, Army
from django.db.models.functions import Lower


def all_miniatures(request):
    """ A view to show all miniatures, including sorting and search queries """

    miniatures = Miniature.objects.all()
    query = None
    gamesys = None
    army = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                miniatures = miniatures.annotate(lower_name=Lower('name'))
            if sortkey == 'gamesys':
                sortkey = 'gamesys__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            miniatures = miniatures.order_by(sortkey)

        if 'gamesys' in request.GET:
            gamesys = request.GET['gamesys'].split(',')
            miniatures = miniatures.filter(
                                    gamesys__name__in=gamesys)
            gamesys = GamingSystem.objects.filter(
                                                name__in=gamesys)

        if 'army' in request.GET:
            army = request.GET['army'].split(',')
            miniatures = miniatures.filter(
                                    army__name__in=army)
            army = Army.objects.filter(
                                name__in=army)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('miniatures'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            miniatures = miniatures.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'miniatures': miniatures,
        'search_term': query,
        'current_gamesys': gamesys,
        'current_army': army,
        'current_sorting': current_sorting,
    }

    return render(request, 'miniatures/miniatures.html', context)


def miniature_details(request, miniature_id):
    """ A view to show individual miniature details """

    miniature = get_object_or_404(Miniature, pk=miniature_id)

    context = {
        'miniature': miniature,
    }

    return render(request, 'miniatures/miniature_details.html', context)
