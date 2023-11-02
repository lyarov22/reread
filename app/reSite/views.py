from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from reread import settings
from .models import Category, Advertisement, Profile, Book
from .forms import RegistrationForm, LoginForm, ProfileForm, AdvertisementForm

default_advertisement_avatar_url = settings.MEDIA_URL + 'book_avatars/default_avatar.png'  # Путь к фотографии по умолчанию
default_user_avatar_url = settings.MEDIA_URL + 'user_avatars/default_avatar.png'  # Путь к фотографии по умолчанию

def index(request):
   
    return render(request, "index.html")


# login system
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входить пользователя после успешной регистрации
            return redirect('reSite:index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reSite:index')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('reSite:index')


# profile system
@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не существует, создайте его здесь
        profile = Profile(user=request.user)
        profile.save()
    
    return render(request, 'profile/view_profile.html', {'profile': profile, 'default_avatar_url': default_user_avatar_url})

@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Если профиль не существует, создайте его здесь
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('reSite:view_profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form, 'profile': profile, 'default_avatar_url': default_user_avatar_url})

@login_required
def create_listing(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect('reSite:listings')  # Перенаправление на страницу со списком объявлений
    else:
        form = AdvertisementForm()
    
    return render(request, 'books/create_listing.html', {'form': form})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Advertisement.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # products = products.filter(category=category)
        products = Advertisement.objects.filter(book__category=category)
        
    return render(request,
                  'books/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                    'default_avatar_url': default_advertisement_avatar_url,
                    })


def book_listing_detail(request, slug):
    advertisement = get_object_or_404(Advertisement, slug=slug)
    book = get_object_or_404(Book, advertisement = advertisement)

    return render(request, 'books/detail.html', 
                  {'advertisement': advertisement, 
                   'default_avatar_url': default_advertisement_avatar_url,
                   'book': book})


@login_required
def edit_listing(request, slug):
    product = get_object_or_404(Advertisement, slug=slug)
    
    # ЧЕТО СЛОМАЛОСЬ
    # # Проверяем, что текущий пользователь является продавцом объявления
    # if Advertisement.seller != request.user:
    #     return redirect('reSite:index')  # Если текущий пользователь не является продавцом, перенаправляем его

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('reSite:book_listing_detail', slug=slug)
    else:
        form = AdvertisementForm(instance=product)

    return render(request, 'books/edit.html', {'form': form, 'product': product})

@login_required
def user_books(request):
    # Получите текущего пользователя
    user = request.user

    # Извлеките все объявления, созданные текущим пользователем
    user_products = Advertisement.objects.filter(seller=user)

    context = {
        'user_products': user_products
    }

    return render(request, 'profile/user_books.html', context)