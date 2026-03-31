# from .models import Profile
from django.shortcuts import render
from bestiary.models import Monster
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_monsters = []
        total_monsters = 0

        # when loged in
        if self.request.user.is_authenticated and hasattr(self.request.user, 'profile'):
            user_profile = self.request.user.profile
            user_monsters = Monster.objects.filter(hunter = user_profile)

            recent_monsters = user_monsters.order_by('-id')[:3]
            total_monsters = user_monsters.count()

        context['recent_monsters'] = recent_monsters
        context['total_monsters'] = total_monsters

        return context

def custom_404(request, exception):
    return render(request, '404.html', status =404)