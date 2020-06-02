from django.contrib import admin
from .models import *


class IngredientInLine(admin.TabularInline):
    model = Ingredient
    extra = 3


# admin.site.register(Recipe, RecipeAdmin)
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInLine]

    list_display= ('title', 'author', 'status', 'publish')
    list_filter = ('status', 'preparation_time_in_minutes', 'publish', 'author')
    search_fields= ('title', 'description')
    raw_id_fields = ('author', )
    date_hierarhy = 'publish'
    ordering = ('status', 'publish')
