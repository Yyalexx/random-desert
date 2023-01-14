from flask import Flask, request, jsonify, render_template
import json
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return render_template('index.html')

#Обрабочик запросов
@app.route('/api/add_message', methods=['GET', 'POST'])
def add_message():
    # получаем JSON со страницы
    content = request.json 
    #тут у нас есть JSON с наименованием блюда
        
    # отдаем JSON с рецептом
    return jsonify(save_recipe(content['food']))



def save_recipe(name):
    with open("5_recipes.json") as recipes:  # ссылка на JSON файл с рецептами
        data = json.load(recipes)

        for key in data.keys():
            if data[key]["recipe_name"]==name:  # находим запрашиваемый рецепт в JSON файле
                recipe = data[key]
                
                return recipe
        else:        
            return {"recipe":'SVEKLU V KASTRULU KIN EPTA I VOT TEBE ' + name}
    

if __name__ == '__main__':
    app.run(port=5000,debug=True)