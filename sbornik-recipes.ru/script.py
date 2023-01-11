import json


def print_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON-файл с рецептами
        data = json.load(recipes)

        for field in data:
            if field["recipe_name"] == name:
                print(field["recipe_name"])  # вывод названия рецепта
                print("\nНеобходимые ингридиенты:")
                for i in field["ingredients"].keys():
                    print(f'{i} : {field["ingredients"][i]}')  # вывод ингридиентов
                print("\nСпособ приготовления:")
                print(f'{field["text"]}\n')  # вывод инструкции по приготовлению


def save_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON файл с рецептами
        data = json.load(recipes)

        for recipe in data:
            if recipe["recipe_name"] == name:  # находим запрашиваемый рецепт в JSON файле
                with open("data.json", "w") as jsonfile:
                    json.dump(recipe, jsonfile, ensure_ascii=False)  # сохранение одного рецепта в отдельном JSON файле


# Примеры запуска функций:
print_recipe("Суп из сёмги с красной чечевицей рецепт на 3 порции (Европейская кухня)")
save_recipe("Курица с кабачками в духовке рецепт на 4 порции (Европейская кухня)")
