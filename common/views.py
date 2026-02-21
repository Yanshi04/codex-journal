# from .models import Profile
from django.shortcuts import render
from bestiary.models import Monster

def home_page(request):
    recent_monsters = Monster.objects.all().order_by('-id')[:3]
    total_monsters = Monster.objects.count()
    context = {
        'recent_monsters': recent_monsters,
        'total_monsters': total_monsters

    }
    return render(request, 'common/home.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status =404)