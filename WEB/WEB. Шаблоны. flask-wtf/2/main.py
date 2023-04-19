from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title: str):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/trainging/<prof>')
def training(prof: str):
    prof = prof.lower()
    params = {'is_engineer': 'инженер' in prof or 'строитель' in prof, 'science_img_url': url_for(
        'static', filename='img/science_map.jpg'), 'engineer_img_url': url_for(
        'static', filename='img/engineer_map.jpg')}
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
