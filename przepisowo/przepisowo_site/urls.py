from django.urls import path
from . import views

app_name = 'przepisowo_site'

urlpatterns = [
    path('', views.RecipesListView.as_view(), name='recipes-list'),
    path('recipe/<str:slug>-<int:pk>/',
         views.RecipeDetailView.as_view(), name='recipe-detail'),

]
