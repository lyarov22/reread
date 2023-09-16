from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from reread import settings
from .models import Profile, BookListing
from .forms import RegistrationForm, LoginForm, ProfileForm, BookListingForm

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
    default_avatar_url = settings.MEDIA_URL + 'avatars/default_avatar.jpg'  # Путь к фотографии по умолчанию
    return render(request, 'profile/view_profile.html', {'profile': profile, 'default_avatar_url': default_avatar_url})

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

    return render(request, 'profile/edit_profile.html', {'form': form})


def create_listing(request):
    if request.method == 'POST':
        form = BookListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect('reSite:listings')  # Перенаправление на страницу со списком объявлений
    else:
        form = BookListingForm()
    
    return render(request, 'listing/create_listing.html', {'form': form})

def listing_list(request):
    listings = BookListing.objects.all()
    return render(request, 'listing/listing_list.html', {'listings': listings})


def book_listing_detail(request, slug):
    book = get_object_or_404(BookListing, slug=slug)
    return render(request, 'listing/book_listing_detail.html', {'book': book})