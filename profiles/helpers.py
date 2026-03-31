# profiles/helpers.py
from .models import Profile

def get_hunter_profile(request):
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        return {'profile': request.user.profile}

    return {'profile': None}