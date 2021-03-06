from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required


class RecipesListView(ListView):
    queryset = Recipe.objects.filter(status="published")
    query_pk_and_slug = True
    paginate_by = 8
    template_name = "recipes_list.html"
    context_object_name = "recipes_list"
    ordering = ["-id"]


class RecipeDetailView(DetailView):
    model = Recipe
    query_pk_and_slug = True
    template_name = "recipe_detail.html"


@login_required
def user_favourites(request):
    return render(request, "favourites.html")
