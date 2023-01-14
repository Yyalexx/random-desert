from flask import Flask, render_template, request


app = Flask(__name__)

dic = {'fsgrgsre': '012', 'grywreg': '1000', 'fagareg': '2'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food = request.form.get('food')
        print(food)
        print(isinstance(food, str))
    return render_template('index.html', dic=dic)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=5000)
