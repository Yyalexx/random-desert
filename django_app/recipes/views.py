from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.db.models import Q
from .filters import RecipeFilter
from .models import Recipe, Connections, Ingredient
from django.core.paginator import Paginator


class RecipesSearch(ListView):
    model = Recipe
    ordering = 'name_recipe'
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 10

    def get_filter(self):
        return RecipeFilter(self.request.GET, queryset=super().get_queryset())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        paginated_filtered_recipes = Paginator(RecipeFilter(self.request.GET, queryset=self.get_queryset()).qs, 10)
        page_number = self.request.GET.get('page')
        recipe_page_obj = paginated_filtered_recipes.get_page(page_number)
        context['recipe_page_obj'] = recipe_page_obj
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


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 10

    def get_queryset(self):
        recipe = self.request.GET.get('recipe')
        cuisines = self.request.GET.getlist('cuisine')
        meal_types = self.request.GET.getlist('meal_type')
        print(recipe)
        print(cuisines)
        print(meal_types)

        if len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) > 0:
            queryset = Recipe.objects.filter(
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) == 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) == 0 and len(meal_types) > 0:
            queryset = Recipe.objects.filter(meal_type__in=meal_types)
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) == 0:
            queryset = Recipe.objects.filter(cuisine__in=cuisines)
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) == 0:
            queryset = Recipe.objects.filter(name_recipe__icontains=recipe)
            return queryset
        else:
            queryset = Recipe.objects.all()
            return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        paginated_filtered_recipes = Paginator(RecipeFilter(self.request.GET, queryset=self.get_queryset()).qs, 10)
        page_number = self.request.GET.get('page')
        recipe_page_obj = paginated_filtered_recipes.get_page(page_number)
        context['recipe_page_obj'] = recipe_page_obj
        return context


class GPTView(TemplateView):
    template_name = 'gpt.html'
