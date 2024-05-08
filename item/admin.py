from django.contrib import admin
from .models import Category
from modeltranslation.admin import TranslationAdmin

class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)