from django.contrib import admin
from .models import Category, Item
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)