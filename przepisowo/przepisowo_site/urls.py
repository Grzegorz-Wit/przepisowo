from django.urls import path
from .views import RecipesListView, RecipeDetailView

app_name = 'przepisowo_site'

urlpatterns = [
    path('', RecipesListView.as_view(), name='recipes-list'),
    path('recipe/<str:slug>-<int:pk>/',
         RecipeDetailView.as_view(), name='recipe-detail'),
]
