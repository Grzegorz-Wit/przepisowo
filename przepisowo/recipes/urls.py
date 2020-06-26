from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.RecipesListView.as_view(), name="recipes-list"),
    path(
        "recipe/<str:slug>-<int:pk>/",
        views.RecipeDetailView.as_view(),
        name="recipe-detail",
    ),
    path("favourites/", views.user_favourites, name="favourites"),
]
