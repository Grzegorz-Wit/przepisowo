from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


class Recipe(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish',
                            null=True,
                            )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               null=True)
    description = models.TextField(null=True)
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=10,
    	choices=STATUS_CHOICES,
    	default='draft')
    image = models.ImageField(null=True, blank=True)

    def get_ingredients(self):
        ingredients = Ingredient.objects.filter(recipe=self)
        return ingredients

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=15, null=True, blank=True)
    recipe = models.ForeignKey(Recipe,
                               related_name='ingredients',
                               on_delete=models.CASCADE,
                               null=True)

    def __str__(self):
        return f'{str(self.quantity)} {self.unit} {self.name}'
