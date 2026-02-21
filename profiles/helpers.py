# profiles/helpers.py
from .models import Profile

def get_hunter_profile(request):
    return {'profile': Profile.objects.first()}