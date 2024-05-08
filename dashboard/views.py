from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item
from django.contrib.auth.models import User

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    user = User.objects.get(username="admin")

    return render(request, 'dashboard/index.html', {
        'items': items,
        'user': user,
    })
