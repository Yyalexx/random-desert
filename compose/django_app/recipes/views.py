import json
import os


from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from .models import Recipe, Connections

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
        user_text = 'Придумай, пожалуйста, рецепт блюда со следующими ингредиентами: ' + ', '.join(ingredients) + \
                    '. Выведи его в формате json, название рецепта помести в поле "name", ' \
                    'список ингредиентов помести в поле "spisok", ' \
                    'инструкцию приготовления помести в поле "instruction".'
        user_text_string = 'Придумай, пожалуйста, рецепт блюда со следующими ингредиентами: ' + ', '.join(ingredients)

        # -------------------получение ответа от ChatGPT (!!! использовать строчки по отдельности!!!)-------------------
        # gpt_response_json = self.generate_gpt3_response(user_text)  # Получение ответа в json подобном формате
        # gpt_response = self.generate_gpt3_response(user_text_string)  # Получение ответа в одной строке
        # -------------------получение ответа от ChatGPT (!!! использовать строчки по отдельности!!!)-------------------

        # --------------------------------заглушка с ответами ChatGPT--------------------------------
        gpt_response_json = '{"name": "Рыба с помидорами и сыром в тандыре", ' \
                            '"spisok": ["рыба (филе) - 500г.", "помидоры - 3шт.", "сыр - 150г.", ' \
                            '"чеснок - 3 зубчика", "укроп - 1/2 пучка", "масло растительное - 2 ст. ложки", ' \
                            '"соль - по вкусу", "перец - по вкусу"], ' \
                            '"instruction": "1. Помидоры нарезать крупными кольцами, сыр натереть на мелкой терке, ' \
                            'чеснок мелко нарезать, укроп измельчить. 2. Рыбу нарезать на порции. ' \
                            '3. Взять керамическую тандырную посуду, на дно налить растительное масло. ' \
                            '4. На дно тандыра выложить помидоры, сверху распределить нарезанную рыбу, ' \
                            'посыпать чесноком, солью и перцем. 5. Сверху выложить натертый сыр ' \
                            'и посыпать мелко нарезанным укропом. 6. Закрыть тандыр крышкой и поставить в духовку ' \
                            'на 40-50 минут при температуре 180 градусов"}'
        gpt_response = 'Предлагаю приготовить рыбу в сырно-помидорном соусе. Ингредиенты: 4 куска рыбы ' \
                       '(например, тилапия или треска), 2 больших помидора, нарезанных кубиками, ' \
                       '1 чашка тертого сыра (например, чеддер или моцарелла), 2 столовые ложки оливкового масла, ' \
                       'соль и перец по вкусу. Инструкции: Разогрейте духовку до 200 градусов. ' \
                       'Разогрейте оливковое масло в большой сковороде на среднем огне. ' \
                       'Обжарьте помидоры до мягкости, примерно 5 минут. ' \
                       'Добавьте в сковороду рыбу и обжаривайте ее до золотистой корочки с обеих сторон, ' \
                       'примерно по 3-4 минуты на каждую сторону. Уберите сковороду с огня, ' \
                       'посолите и поперчите по вкусу. Посыпьте тертым сыром сверху рыбы и помидоров. ' \
                       'Перенесите сковороду в духовку и готовьте, пока сыр не растает ' \
                       'и не станет золотистого цвета, примерно 5-7 минут. ' \
                       'Ваша рыба в сырно-помидорном соусе готова! ' \
                       'Подайте ее горячей с любимой гарниром или овощным салатом.'

        # --------------------------------заглушка с ответами ChatGPT--------------------------------

        gpt_response_dict = json.loads(gpt_response_json, strict=False)
        context['gpt_recipe_name'] = gpt_response_dict['name']
        context['gpt_recipe_ingredients'] = gpt_response_dict['spisok']
        context['gpt_recipe_description'] = gpt_response_dict['instruction']

        context['gpt_recipe'] = gpt_response

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
