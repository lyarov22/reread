from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),

    path('create-item/', views.create_item, name='create_item'),
    path('search-books/', views.search_books, name='search_books'),
    path('submit_book_suggestion/', views.submit_book_suggestion, name='submit_book_suggestion'),

    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]
