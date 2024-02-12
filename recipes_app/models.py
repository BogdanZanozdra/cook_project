from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cooking_steps = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'
