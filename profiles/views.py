from django.shortcuts import render, redirect
from .forms import ProfileCreateForm

def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form
    }

    return render(request, 'profiles/profile-create.html', context)