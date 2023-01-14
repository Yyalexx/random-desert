from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food = request.form.get('food')
        return render_template('index.html', rec=save_recipe(food))
    return render_template('index.html')


def save_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON файл с рецептами
        data = json.load(recipes)
        for key in data.keys():
            if name.lower() in data[key]["recipe_name"].lower():  # находим запрашиваемый рецепт в JSON файле
                recipe = data[key]
                return recipe
        else:
            return {"recipe": 'SVEKLU V KASTRULU KIN EPTA I VOT TEBE ' + name}


save_recipe('Курица')


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=5000)
