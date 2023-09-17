from django.contrib import admin
from .models import BookListing

@admin.register(BookListing)
class BookListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller')
