from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title: str):
    params = {'title': title}
    return render_template('base.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
