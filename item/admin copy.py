from django.contrib import admin
from django import forms
from .models import Category, Item
import json

class CategoryAdminForm(forms.ModelForm):
    en_name = forms.CharField(label='English Name', max_length=255, required=False)
    kk_name = forms.CharField(label='Kazakh Name', max_length=255, required=False)
    ru_name = forms.CharField(label='Russian Name', max_length=255, required=False)
    json_data = forms.CharField(label='JSON Data', widget=forms.Textarea, required=False)

    class Meta:
        model = Category
        fields = ['en_name', 'kk_name', 'ru_name', 'json_data']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['en_name'].initial = self.instance.get_name('en')
            self.fields['kk_name'].initial = self.instance.get_name('kk')
            self.fields['ru_name'].initial = self.instance.get_name('ru')
            self.fields['json_data'].initial = json.dumps(self.instance.name_translations, ensure_ascii=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        en_name = self.cleaned_data.get('en_name')
        kk_name = self.cleaned_data.get('kk_name')
        ru_name = self.cleaned_data.get('ru_name')
        json_data = self.cleaned_data.get('json_data')

        if en_name and kk_name and ru_name:
            instance.name_translations = {
                'en': en_name,
                'kk': kk_name,
                'ru': ru_name,
            }
        elif json_data:
            instance.name_translations = json.loads(json_data)

        if commit:
            instance.save()
        return instance

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    list_display = ['name', 'display_image']
    search_fields = ['name']
    fields = ['name', 'image', 'en_name', 'kk_name', 'ru_name', 'json_data']
    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
