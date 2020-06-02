from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView


class RecipesListView(ListView):

    model = Recipe
    paginate_by = 20
    template_name = 'recipes_list.html'


class RecipeDetailView(DetailView):

    model = Recipe
    template_name = 'recipe_detail.html'
