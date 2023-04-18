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


def render_page(nick: str, level: int, raiting: float):
    str_level = str(level)
    str_raiting = str(raiting)
    code = get_code('index')
    return code.replace('%NICK%', nick).replace('%LEVEL%', str_level).replace('%RAITING%', str_raiting)


@app.route('/results/<nick>/<int:level>/<float:raiting>')
def results(nick: str, level: int, raiting: int):
    return render_page(nick, level, raiting)


@app.errorhandler(404)
def page_not_found(error):
    return get_code('not_found')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
