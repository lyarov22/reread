from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', blank=False, default='default.jpg')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Item(models.Model):
    CONDITION_CHOICES = [
        ('Н', 'Новая'),
        ('О', 'Отличное'),
        ('Х', 'Хорошее'),
        ('С', 'Среднее'),
        ('П', 'Плохое'),
    ]
    
    COVER_CHOICES = [
        ('Т', 'Твердый переплет'),
        ('М', 'Мягкая обложка'),
        ('К', 'Переплет из картона'),
        ('И', 'Интегральный переплет'),
        ('С', 'Суперобложка'),
        ('Д', 'Другой'),
    ]

    LANGUAGE_CHOICES = [
        ('RU', 'Русский'),
        ('KZ', 'Казахский'),
        ('EN', 'Английский'),
        ('OT', 'Другой'),
    ]

    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=100, verbose_name="Издательство")
    
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык")
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES, verbose_name="Состояние книги")
    cover_type = models.CharField(max_length=1, choices=COVER_CHOICES, verbose_name="Переплет")

    description = models.TextField(blank=True, null=True)

    price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=0, validators=[MinValueValidator(0)], verbose_name="Цена")
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    
    image1 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='item_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='item_images/', blank=True, null=True)

    is_sold = models.BooleanField(default=False)
    is_swap = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"