from django.shortcuts import render, redirect
from .forms import ProfileCreateForm
from .models import Profile

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

def profile_details(request):
    profile=Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'profiles/profile-details.html', context)

def profile_edit(request):
    profile=Profile.objects.first()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileCreateForm(instance=profile)

    context = {'form': form, 'profile': profile}
    return render(request, 'profiles/profile-edit.html', context)

def profile_delete(request):
    profile=Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {'profile': profile}
    return render(request, 'profiles/profile-delete.html', context)