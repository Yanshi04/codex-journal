from django.shortcuts import render
from profiles.models import Profile

def home_page(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/home.html', context)