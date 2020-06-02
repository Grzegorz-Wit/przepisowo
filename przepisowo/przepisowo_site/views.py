from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView


class RecipesListView(ListView):

    model = Recipe
    query_pk_and_slug = True
    paginate_by = 10
    template_name = 'recipes_list.html'


class RecipeDetailView(DetailView):

    model = Recipe
    query_pk_and_slug = True
    template_name = 'recipe_detail.html'
