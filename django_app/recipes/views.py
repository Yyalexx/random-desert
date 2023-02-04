from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .filters import RecipeFilter
from .models import Recipe, Connections, Ingredient


class RecipesSearch(ListView):
    model = Recipe
    ordering = 'name_recipe'
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 1

    def get_filter(self):
        return RecipeFilter(self.request.GET, queryset=super().get_queryset())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context


class RecipeDetails(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connections'] = Connections.objects.all()
        return context


class ConnectionsDetails(DetailView):
    model = Connections
    template_name = 'recipe.html'
    context_object_name = 'connections'

