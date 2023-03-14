from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Recipe, Connections


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


class GPTView(TemplateView):
    template_name = 'gpt.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class SearchView(ListView):
    model = Recipe
    ordering = 'name_recipe'
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 16

    def get_queryset(self):
        recipe = self.request.GET.get('recipe')
        cuisines = self.request.GET.getlist('cuisine')
        meal_types = self.request.GET.getlist('meal_type')
        ingredients = self.request.GET.getlist('ingredients')

        if len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) > 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) > 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) > 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(meal_type__in=meal_types) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) == 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) > 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) > 0 and len(meal_types) == 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(cuisine__in=cuisines)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) > 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) == 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(name_recipe__icontains=recipe) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) > 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(
                Q(cuisine__in=cuisines) &
                Q(meal_type__in=meal_types)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) == 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(cuisine__in=cuisines) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) == 0 and len(meal_types) > 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(
                Q(meal_type__in=meal_types) &
                Q(connections__id_ingr__group_name_ingr__in=ingredients)
            )
            return queryset
        elif len(recipe) == 0 and len(cuisines) == 0 and len(meal_types) > 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(meal_type__in=meal_types)
            return queryset
        elif len(recipe) == 0 and len(cuisines) > 0 and len(meal_types) == 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(cuisine__in=cuisines)
            return queryset
        elif len(recipe) > 0 and len(cuisines) == 0 and len(meal_types) == 0 and len(ingredients) == 0:
            queryset = Recipe.objects.filter(name_recipe__icontains=recipe)
            return queryset
        elif len(recipe) == 0 and len(cuisines) == 0 and len(meal_types) == 0 and len(ingredients) > 0:
            queryset = Recipe.objects.filter(connections__id_ingr__group_name_ingr__in=ingredients)
            return queryset
        else:
            queryset = Recipe.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_queryset()
        paginated_filtered_recipes = Paginator(self.get_queryset(), 16)
        page_number = self.request.GET.get('page')
        recipe_page_obj = paginated_filtered_recipes.get_page(page_number)
        context['recipe_page_obj'] = recipe_page_obj
        recipe = self.request.GET.get('recipe')
        cuisines = self.request.GET.getlist('cuisine')
        meal_types = self.request.GET.getlist('meal_type')
        ingredients = self.request.GET.getlist('ingredients')
        context['search_params'] = ""
        if len(recipe) != 0:
            context['search_params'] += f'{recipe}, '
        if len(cuisines) != 0:
            for cuisine in cuisines:
                context['search_params'] += f'{cuisine}, '
        if len(meal_types) != 0:
            for meal_type in meal_types:
                context['search_params'] += f'{meal_type}, '
        if len(ingredients) != 0:
            for ingredient in ingredients:
                context['search_params'] += f'{ingredient}, '
        if len(context['search_params']) != 0:
            context['search_params'] = context['search_params'][:-2]
        else:
            context['search_params'] = 'Покажите всё'

        return context
