from django.shortcuts import render
from profiles.models import Profile
from bestiary.models import Monster

def home_page(request):
    profile = Profile.objects.first()
    recent_monsters = Monster.objects.all().order_by('-id')[:3]
    total_monsters = Monster.objects.count()
    context = {
        'profile': profile,
        'recent_monsters': recent_monsters,
        'total_monsters': total_monsters
    }
    return render(request, 'common/home.html', context)

def custom_404(request, exception):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, '404.html', context, status=404)