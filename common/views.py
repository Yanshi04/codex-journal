from django.shortcuts import render
from profiles.models import Profile

def home_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/home.html', context)

def custom_404(request, exception):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, '404.html', context, status=404)