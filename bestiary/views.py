from django.shortcuts import render, redirect, get_object_or_404

from .forms import MonsterForm
from .models import Monster
from profiles.models import Profile

def bestiary_list(request):
    sort_by = request.GET.get('sort', 'name_asc')
    if sort_by == 'name_desc':
        all_monsters = Monster.objects.all().order_by('-monster_name')
    elif sort_by == 'danger':
        all_monsters = Monster.objects.all().order_by('-level_of_danger')
    else:
        # Default: Name A-Z
        all_monsters = Monster.objects.all().order_by('monster_name')

    profile = Profile.objects.first()

    context = {'monsters': all_monsters, 'profile': profile, 'current_sort': sort_by}
    return render(request, 'bestiary/bestiary_list.html', context)

def add_monster(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = MonsterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bestiary_list')
    else:
        form = MonsterForm()
    context = {'form': form, 'profile': profile}
    return render(request, 'bestiary/monster_create.html', context)

def monster_details(request, pk):
    profile = Profile.objects.first()
    monster = get_object_or_404(Monster, pk=pk)
    context = {'monster': monster, 'profile': profile}
    return render(request, 'bestiary/monster_details.html', context)

def edit_monster(request, pk):
    monster = get_object_or_404(Monster, pk=pk )
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = MonsterForm(request.POST, instance = monster)
        if form.is_valid():
            form.save()
            return redirect('monster_details', pk =monster.pk)
    else:
        form = MonsterForm(instance = monster)
    context = {'form': form, 'monster': monster, 'profile': profile}
    return render(request, 'bestiary/monster_edit.html', context)

def delete_monster(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    profile = Profile.objects.first()
    if request.method == 'POST':
        monster.delete()
        return redirect('bestiary_list')
    return render(request, 'bestiary/monster_confirm_delete.html', {'monster': monster, 'profile': profile})