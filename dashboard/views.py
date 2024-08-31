from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm

from item.models import Item
from core.models import CustomUser

@login_required
def index(request):
    items = Item.objects.filter(user=request.user)
    user = CustomUser.objects.get(username=request.user.username)

    return render(request, 'dashboard/profile.html', {
        'items': items,
        'user': user,
    })


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')  # Перенаправление на страницу профиля после успешного сохранения
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'dashboard/edit_profile.html', {'form': form})
