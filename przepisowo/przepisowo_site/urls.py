from django.urls import path
from .views import RecipesListView, RecipeDetailView

urlpatterns = [
	path('', RecipesListView.as_view(), name='recipes'),
	path('recipe/<int:pk>/', RecipeDetailView.as_view(), name ='recipe'),

]