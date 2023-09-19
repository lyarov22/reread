from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'reSite'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/reread-logo.ico', permanent=True), name='favicon'),
    path('', views.index, name='index'),

    # login system
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # profile system
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),


    path('create_listing/', views.create_listing, name='create_listing'),

    path('books', views.product_list, name='listings'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    path('books/<slug:slug>/', views.book_listing_detail, name='book_listing_detail'),

    path('books/<slug:slug>/edit/', views.edit_listing, name='edit_listing'),

    path('profile/books', views.user_books, name='user_books'),
    
]