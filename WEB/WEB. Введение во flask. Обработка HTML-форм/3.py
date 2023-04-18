from flask import Flask, app

PROMOTION = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

IMAGE_URL = 'https://downloader.disk.yandex.ru/preview/a2e340147273698778a52b' + \
    '21c642d5d1544dff1bdbfaae30f95ba6efc122abfa/63e54b87/MlVGFEVvuq6L0nuBZ4O3' + \
    'RTt9DLcYUZHL8TSQhHRnEPkrln7foL1ikiJSAxujdcMFOTbxAyOl2c53Ba4mkAlsow%3D%3D' + \
    '?uid=0&filename=mars.png&disposition=inline&hash=&limit=0&content_type=i' + \
    'mage%2Fpng&owner_uid=0&tknv=v2&size=2048x2048'
app = Flask(__name__)


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return '<br/>'.join(PROMOTION)


@app.route('/image_mars')
def image():
    return f"""
    <!DOCTYPE html>
    <head>
    <title>Привет, Марс!</title>
    </head>
    <body>
    <h1>Жди нас, Марс!</h1>
    <img src="{IMAGE_URL}" width="300"/>
    <p>Вот она какая, красная планета</p>
    </body>
    """


if __name__ == '__main__':
    app.run(port='8080', host='127.0.0.1')
