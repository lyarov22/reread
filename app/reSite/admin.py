from django.contrib import admin
from .models import Advertisement, Category, Book, Profile

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('price', 'seller')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass