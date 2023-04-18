from flask import Flask
from os.path import join

app = Flask(__name__)

possible_names = {'mars', 'venera', 'mercury'}


def render_page(name: str) -> str:
    path = join('static', 'html', name + '.html')
    file = open(path)
    data = file.read()
    file.close()
    del file
    return data


@app.route('/')
def index():
    return render_page('index')


@app.route('/choice/<name>')
def choice(name: str):
    if name in possible_names:
        return render_page(name)
    else:
        return render_page('not_found')


@app.errorhandler(404)
def page_not_found(error):
    return render_page('not_found')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
