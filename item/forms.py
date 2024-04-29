from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Item, Category

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class CategoryChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        self.language_code = kwargs.pop('language_code', None)
        super().__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return getattr(obj, f'name_{self.language_code}', obj.name)

class NewItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        language_code = kwargs.pop('language_code', None)
        super().__init__(*args, **kwargs)
        self.fields['category'] = CategoryChoiceField(queryset=Category.objects.all(), empty_label=_('Select a category'), language_code=language_code)

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES})
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES})
        }
