from django.contrib import admin
from .models import Book, Category, Publisher
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book)
admin.site.register(Publisher)