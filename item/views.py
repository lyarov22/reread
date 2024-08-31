from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import BookSearchForm, NewItemForm
from .models import Book, Category, Item, ItemImage

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    images = ItemImage.objects.filter(item=item)

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'images': images,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            uploaded_images = request.FILES.getlist('images')
            for image in uploaded_images:
                ItemImage.objects.create(item=item, image=image)

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item = form.save()

            if 'images' in request.FILES:
                ItemImage.objects.filter(item=item).delete()
                uploaded_images = request.FILES.getlist('images')
                for image in uploaded_images:
                    ItemImage.objects.create(item=item, image=image)

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

def search_books(request):
    query = request.GET.get('query', '')
    books = Book.objects.filter(name__icontains=query)
    book_list = [{'id': book.id, 'name': book.name} for book in books]
    return JsonResponse({'books': book_list})

def create_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            # Redirect or process as needed
    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {'form': form, 'title': 'Create Item'})

def submit_book_suggestion(request):
    if request.method == 'POST':
        suggestion = request.POST.get('new_book_title')
        # Здесь можно сохранить предложение в базу данных или отправить уведомление модераторам
        messages.success(request, 'Your book suggestion has been sent for review.')
        return redirect('create_item')
    return redirect('create_item')