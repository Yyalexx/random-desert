from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food = request.form.get('food')
        return render_template('index.html', rec=save_recipe(food))
    return render_template('index.html', rec=best_recipes())


def best_recipes(): #пока просто первые рецепты из файла, чтобы начальная страница не была пустой
    with open("16_recipes.json", encoding='utf-8') as recipes:
        data = json.load(recipes)
        recipe_list, counter = [], 5
        for ind in data['recipe_id']:
            recipe_list.append(data['recipe_id'][ind])
            counter -= 1
            if counter == 0:
                break
        return recipe_list


def save_recipe(name):
    with open("16_recipes.json", encoding='utf-8') as recipes:  # ссылка на JSON файл с рецептами
        data = json.load(recipes)
        recipe_list = []
        for ind in data['recipe_id']:
            if name.lower() in data['recipe_id'][ind]['recipe_name'].lower():  # находим запрашиваемый рецепт в JSON файле
                recipe_list.append(data['recipe_id'][ind])
        return recipe_list
        # else:
        #     return {"recipe_name": name, "ingredients": [name], "text": "Чтобы приготовить " + name.lower() + ", делаем следующее: берем "+ name.lower() + ", добавляем специи по вкусу и доводим до готовности."}


# save_recipe('Курица')


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=5000)
