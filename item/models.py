from django.conf import settings
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='category_images', blank=False, default='default.jpg')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/images/book/')
    created_at = models.DateTimeField(auto_now_add=True)


# Модель предмета (Item)
class Item(models.Model):
    CONDITION_CHOICES = [
        ('A', 'Новая'),
        ('B', 'Отличное'),
        ('C', 'Хорошее'),
        ('D', 'Среднее'),
        ('F', 'Плохое'),
    ]

    COVER_CHOICES = [
        ('A', 'Твердый'),
        ('B', 'Мягкий'),
        ('X', 'Другой'),
    ]

    LANGUAGE_CHOICES = [
        ('RU', 'Русский'),
        ('KZ', 'Казахский'),
        ('EN', 'Английский'),
        ('DE', 'Немецкий'),
        ('OT', 'Другой'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='items')
    
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name="Язык")
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES, verbose_name="Состояние книги")
    cover_type = models.CharField(max_length=1, choices=COVER_CHOICES, verbose_name="Переплет")

    description = models.TextField(blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_swap = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/images/item/')
    created_at = models.DateTimeField(auto_now_add=True)