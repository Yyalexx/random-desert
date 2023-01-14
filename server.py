from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Аюна громко пукает'

#Обрабочик запросов
#Тут надо добавить, чтобы инфу он брал из наших файлов с данными или БД
@app.route('/api/add_message', methods=['GET', 'POST'])
def add_message():
    # получаем JSON со страницы
    content = request.json 
    # print(content['food'])
    
    # отдаем JSON с рецептом
    return jsonify({"recipe":'SVEKLU V KASTRULU KIN EPTA I VOT TEBE ' + content['food']})


if __name__ == '__main__':
    app.run(port=5000,debug=True)