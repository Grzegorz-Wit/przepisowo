from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Recipe(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=200)
    subname = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(default="", editable=False, max_length=200,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    image = models.ImageField(blank=True)
    preparation_time_in_minutes = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "pk": self.id}
        return reverse("recipes:recipe-detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=15, blank=True)
    recipe = models.ForeignKey(
        Recipe, related_name="ingredients", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"
