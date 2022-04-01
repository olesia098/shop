from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


User = get_user_model()


class Category(models.Model):
    slug = models.SlugField(max_length=30, primary_key=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.slug


class Product(models.Model):
    owner = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)#ограничение
    description = models.TextField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True) #делает это поле не обязательным # работает с картинками

    def __str__(self):
        return self.name