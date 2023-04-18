from flask import Flask
from os.path import join

app = Flask(__name__)


def get_code(name: str):
    filepath = join('static', 'html', name + '.html')
    file = open(filepath)
    code = file.read()
    file.close()
    del file
    return code


@app.route('/')
def results():
    return get_code('index')


@app.errorhandler(404)
def page_not_found(error):
    return get_code('not_found')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
