from django.shortcuts import render

def home_page(request):
	context = {}
	return render(request, 'przepisowo/home.html', context)

def recipe(request):
	context = {}
	return render(request, 'przepisowo/recipe.html', context)