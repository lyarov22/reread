import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# login system
class CustomUser(AbstractUser):
    # Добавьте здесь дополнительные поля, если необходимо
    pass



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username



class BookListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Добавьте другие поля, например, фотографии книги
    slug = models.SlugField(unique=True, max_length=200, allow_unicode=True, null=True, blank=True)

    unique_number = models.PositiveIntegerField(unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем случайное уникальное число
            self.unique_number = random.randint(1000000, 9999999)
            self.slug = slugify(f"{self.title}-{self.unique_number}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_listing_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title