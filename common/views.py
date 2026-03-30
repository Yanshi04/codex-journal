# from .models import Profile
from django.shortcuts import render
from bestiary.models import Monster
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_monsters'] = Monster.objects.all().order_by('-id')[:3]
        context['total_monsters'] = Monster.objects.count()


        return context

def custom_404(request, exception):
    return render(request, '404.html', status =404)