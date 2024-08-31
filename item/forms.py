from django import forms
from .models import Book, Item, ItemImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search for a book', max_length=255, required=False)

class NewItemForm(forms.ModelForm):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        widget=forms.Select(attrs={'id': 'book-select'}),
        required=False
    )
    images = MultipleFileField(label='Select files', required=False)

    class Meta:
        model = Item
        fields = ['book', 'publisher', 'language', 'condition', 'cover_type', 'description', 'price', 'is_swap']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request:
            instance.user = self.request.user
        if commit:
            instance.save()
        return instance
