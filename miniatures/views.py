from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Miniature, GamingSystem, Army
from .forms import MiniatureForm, ArmyForm, GameSystemForm


def all_miniatures(request):
    """ A view to show all miniatures, including sorting and search queries """

    miniatures = Miniature.objects.all()
    query = None
    gamesystems = None
    armies = None
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
            gamesystems = request.GET['gamesys__name'].split(',')
            miniatures = miniatures.filter(
                                    gamesys__name__in=gamesystems)
            gamesystems = GamingSystem.objects.filter(
                                                name__in=gamesystems)

        if 'army' in request.GET:
            armies = request.GET['army__name'].split(',')
            miniatures = miniatures.filter(
                                    army__name__in=armies)
            armies = Army.objects.filter(
                                name__in=armies)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('miniatures'))

            queries = Q(name__icontains=query) | Q(
                                                   description__icontains=query
                                                   ) | Q(
                                                         gamesys__name__icontains=query
                                                         ) | Q(
                                                               army__name__icontains=query
                                                               )
            miniatures = miniatures.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'miniatures': miniatures,
        'search_term': query,
        'current_gamesystems': gamesystems,
        'current_armies': armies,
        'current_sorting': current_sorting,
    }

    return render(request, 'miniatures/miniatures.html', context)


def all_armies(request):
    """ A view to show all armies """
    army = Army.objects.all()


def miniature_details(request, miniature_id):
    """ A view to show individual miniature details """

    miniature = get_object_or_404(Miniature, pk=miniature_id)

    context = {
        'miniature': miniature,
    }

    return render(request, 'miniatures/miniature_details.html', context)


@login_required
def add_miniature(request):
    """ Add a miniature to the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MiniatureForm(request.POST, request.FILES)
        if form.is_valid():
            miniature = form.save()
            messages.success(request, 'Successfully added miniature!')
            return redirect(reverse('miniature_details', args=[miniature.id]))
        else:
            messages.error(request,
                           'Failed to add miniature. Please check that the form is valid.')
    else:
        form = MiniatureForm()

    template = 'miniatures/add_miniature.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_army(request):
    """ Add an army to the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArmyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added army!')
            return redirect(reverse('add_army'))
        else:
            messages.error(request,
                           'Failed to add army. Please check that the form is valid.')
    else:
        form = ArmyForm()

    template = 'miniatures/add_army.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_gamesystem(request):
    """ Add a game system to the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GameSystemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added game system!')
            return redirect(reverse('add_gamesystem'))
        else:
            messages.error(request,
                           'Failed to add game system. Please check that the form is valid.')
    else:
        form = GameSystemForm()

    template = 'miniatures/add_gamesystem.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_miniature(request, miniature_id):
    """ Edit a miniature in the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    miniature = get_object_or_404(Miniature, pk=miniature_id)
    if request.method == 'POST':
        form = MiniatureForm(request.POST, request.FILES, instance=miniature)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {miniature.name}')
            return redirect(reverse('miniature_details', args=[miniature.id]))
        else:
            messages.error(request,
                           f'Failed to update {miniature.name}. Please check that the form is valid.')
    else:
        form = MiniatureForm(instance=miniature)
        messages.info(request, f'You are editing {miniature.name}.')

    template = 'miniatures/edit_miniature.html'
    context = {
        'form': form,
        'miniature': miniature,
    }

    return render(request, template, context)


@login_required
def edit_army(request, army_id):
    """" Edit an army in the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    army = get_object_or_404(Army, pk=army_id)
    if request.method == 'POST':
        form = ArmyForm(request.POST, request.FILES, instance=army)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Successfully updated {army.friendly_name}')
            return redirect(reverse('edit_army', args=[army.id]))
        else:
            messages.error(request,
                           f'Failed to update {army.friendly_name}. Please check that the form is valid.')
    else:
        form = ArmyForm(instance=army)
        messages.info(request, f'You are editing {army.friendly_name}.')

    template = 'miniatures/edit_army.html'
    context = {
        'form': form,
        'army': army,
    }

    return render(request, template, context)


@login_required
def edit_gamesystem(request, gamesystem_id):
    """" Edit an army in the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    gamesystem = get_object_or_404(GamingSystem, pk=gamesystem_id)
    if request.method == 'POST':
        form = GameSystemForm(request.POST, request.FILES, instance=gamesystem)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Successfully updated {gamesystem.friendly_name}')
            return redirect(reverse('edit_gamesystem', args=[gamesystem.id]))
        else:
            messages.error(request,
                           f'Failed to update {gamesystem.friendly_name}. Please check that the form is valid.')
    else:
        form = GameSystemForm(instance=gamesystem)
        messages.info(request, f'You are editing {gamesystem.friendly_name}.')

    template = 'miniatures/edit_gamesystem.html'
    context = {
        'form': form,
        'gamesystem': gamesystem,
    }

    return render(request, template, context)


@login_required
def delete_miniature(request, miniature_id):
    """ Deletes a miniature from the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    miniature = get_object_or_404(Miniature, pk=miniature_id)
    miniature.delete()
    messages.success(request, 'Miniature deleted!')
    return redirect(reverse('miniatures'))


@login_required
def delete_army(request, army_id):
    """ Deletes an army from the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    army = get_object_or_404(Army, pk=army_id)
    army.delete()
    messages.success(request, 'Army deleted!')
    return redirect(reverse('miniatures'))


@login_required
def delete_gamesystem(request, gamesystem_id):
    """ Deletes a game system from the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Access denied, only staff members can do that.')
        return redirect(reverse('home'))

    gamesystem = get_object_or_404(Army, pk=gamesystem_id)
    gamesystem.delete()
    messages.success(request, 'Game System deleted!')
    return redirect(reverse('miniatures'))
