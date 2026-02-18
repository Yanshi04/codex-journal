from django.shortcuts import render, redirect

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