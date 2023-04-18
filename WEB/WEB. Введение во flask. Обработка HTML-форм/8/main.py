from flask import Flask, url_for, request
from os.path import join, exists
from os import makedirs

app = Flask(__name__)


def get_code(name: str):
    filepath = join('static', 'html', name + '.html')
    file = open(filepath)
    code = file.read()
    file.close()
    del file
    css_url = url_for('static', filename='css/main.css')
    return code.replace('%CSSPATH%', css_url)


def render_page(image: str):
    code = get_code('index')
    return code.replace('%IMAGE%', image)


def render_image():
    code = get_code('image')
    filepath = ''
    if exists(join('static', 'img', 'img.png')):
        filepath = url_for('static', filename='img/img.png')
    else:
        filepath = url_for('static', filename='img/img.jpg')
    return code.replace('%PATH%', filepath)


@app.route('/', methods=['GET', 'POST'])
@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_page('')
    else:
        f = request.files['file']
        if not exists(join('static', 'img')):
            makedirs(join('static', 'img'))
        resolution = f.filename.split('.')[-1]
        if resolution == 'jpeg':
            resolution = 'jpg'
        filepath = join('static', 'img', 'img.' + resolution)
        f.save(filepath)
        return render_page(render_image())


@app.errorhandler(404)
def page_not_found(error):
    return get_code('not_found')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
