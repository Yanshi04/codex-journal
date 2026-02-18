from django.shortcuts import render
from .models import Monster

def bestiary_list(request):
    all_monsters = Monster.objects.all()
    context = {'monsters': all_monsters}
    return render(request, 'bestiary/bestiary_list.html', context)