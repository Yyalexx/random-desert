import json


def print_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON-файл с рецептами
        data = json.load(recipes)

        for key in data.keys():
            if data[key]['recipe_name']==name:
                print(data[key]['recipe_name'])  # вывод названия рецепта
                print("\nНеобходимые ингредиенты:")
                for i in data[key]['ingredients'].keys():
                    print(f'{i} : {data[key]["ingredients"][i]}')  # вывод ингредиентов
                print("\nСпособ приготовления:")
                print(f'{data[key]["text"]}\n')  # вывод инструкции по приготовлению


def save_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON файл с рецептами
        data = json.load(recipes)

        for key in data.keys():
            if data[key]['recipe_name']==name:  # находим запрашиваемый рецепт в JSON файле
                recipe = data[key]
                print (recipe)
                with open("data.json", "w") as jsonfile:
                    json.dump(recipe, jsonfile, ensure_ascii=False)  # сохранение одного рецепта в отдельном JSON файле


# Примеры запуска функций:
print_recipe("Суп из сёмги с красной чечевицей рецепт на 3 порции (Европейская кухня)")
save_recipe("Курица с кабачками в духовке рецепт на 4 порции (Европейская кухня)")