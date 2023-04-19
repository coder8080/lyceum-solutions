from flask import Flask, render_template, url_for

app = Flask(__name__)

NAMES = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
         'Венката Капур', 'Тедди Сандерс', 'Шон Бин']


@app.route('/distribution')
def distribution():
    params = {'astronauts': NAMES}
    return render_template('distribution.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
