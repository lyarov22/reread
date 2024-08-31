from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
