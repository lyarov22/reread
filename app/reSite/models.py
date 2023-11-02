import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# login system
class CustomUser(AbstractUser):
    # Добавьте здесь дополнительные поля, если необходимо
    pass



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='user_avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username



# class Product(models.Model):
#     avatar = models.ImageField(upload_to='listing_avatars/', blank=True, null=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True, max_length=200, allow_unicode=True, null=True, blank=True)

#     unique_number = models.PositiveIntegerField(unique=True, editable=False)
    
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             # Генерируем случайное уникальное число
#             self.unique_number = random.randint(1000000, 9999999)
#             self.slug = slugify(f"{self.title}-{self.unique_number}")
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('book_listing_detail', kwargs={'slug': self.slug})

#     def __str__(self):
#         return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('reSite:product_list_by_category',
                        args=[self.slug])

class Book(models.Model):
    avatar = models.ImageField(upload_to='book_avatars/', blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    avatar = models.ImageField(upload_to='advertisement_avatars/', blank=True, null=True)
    # title = models.CharField(max_length=200, db_index=True)
    # description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    source = models.CharField(max_length=255)  # Олх, Флип КЗ, Меломан и т.д.
    condition = models.CharField(max_length=255)  # Новая, б/у, электронная и т.д.
    
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=200, allow_unicode=True, null=True, blank=True)

    unique_number = models.PositiveIntegerField(unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем случайное уникальное число
            self.unique_number = random.randint(1000000, 9999999)
            self.slug = slugify(f"{self.book}-{self.unique_number}")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('price',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"Advertisement: {self.book.title} - {self.price} KZT"

    
    def get_absolute_url(self):
        return reverse('reSite:book_listing_detail', args=[str(self.slug)])
    
class AdvertisementImage(models.Model):
    post = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='Advertisement/%Y/%m/%d/', verbose_name='Дополнительное фото / Қосымша фотосурет')

    def __str__(self):
        return f"{self.post.title} Image"
    
    class Meta:
        verbose_name = 'Изображение / Сурет'
        verbose_name_plural = 'Изображения / Суреттер'