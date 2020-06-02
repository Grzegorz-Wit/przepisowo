from django.contrib import admin
from .models import *
# Register your models here.

class IngredientInLine(admin.TabularInline):
	model = Ingredient
	extra = 3


class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInLine]


admin.site.register(Recipe, RecipeAdmin)