from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', blank=True, null=True, default='default.jpg')
    name_translations = JSONField(verbose_name='Translated Names', blank=True, null=True, default="")

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.get_name()

    def get_name(self, language_code=None):
        if self.name_translations:
            if language_code and language_code in self.name_translations:
                return self.name_translations[language_code]
            else:
                return self.name_translations.get('en', 'No translation available')
        else:
            return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name