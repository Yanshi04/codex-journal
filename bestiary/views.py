from django.shortcuts import render, redirect, get_object_or_404

from .forms import MonsterForm
from .models import Monster

def bestiary_list(request):
    all_monsters = Monster.objects.all()
    context = {'monsters': all_monsters}
    return render(request, 'bestiary/bestiary_list.html', context)

def add_monster(request):
    if request.method == 'POST':
        form = MonsterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bestiary_list')
    else:
        form = MonsterForm()
    context = {'form': form}
    return render(request, 'bestiary/monster_create.html', context)

def monster_details(request, pk):
    monster = get_object_or_404(Monster, pk=pk)
    context = {'monster': monster}
    return render(request, 'bestiary/monster_details.html', context)