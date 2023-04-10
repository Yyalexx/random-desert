import json
import os


from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Recipe, Connections
from .config import gpt_response  # закоментить, если подключаемся к ChatGPT

import openai as ai
from dotenv import load_dotenv

load_dotenv()


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


class GPTResultView(TemplateView):
    template_name = 'gpt_recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        ingredients = self.request.GET.getlist('ingredients')
        context['ingredients'] = ', '.join(ingredients)
        user_text_string = 'Придумай, пожалуйста, рецепт блюда со следующими ингредиентами: ' + ', '.join(ingredients)

        # -------------------получение ответа от ChatGPT -------------------
        # gpt_response = self.generate_gpt3_response(user_text_string)
        # -------------------получение ответа от ChatGPT -------------------

        context['gpt_recipe'] = gpt_response  # openai api или config.py

        return context

    @staticmethod
    def generate_gpt3_response(user_text, print_output=False):
        """
        Query OpenAI GPT-3 for the specific key and get back a response
        :type user_text: str the user's text to query for
        :type print_output: boolean whether or not to print the raw output JSON
        """
        ai.api_key = os.getenv('GPT_API_KEY')

        completions = ai.Completion.create(
            engine='text-davinci-003',  # Determines the quality, speed, and cost.
            temperature=0.5,            # Level of creativity in the response
            prompt=user_text,           # What the user typed in
            max_tokens=1024,             # Maximum tokens in the prompt AND response
            n=1,                        # The number of completions to generate
            stop=None,                  # An optional setting to control response generation
        )

        # Return the first choice's text
        return completions.choices[0].text


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
