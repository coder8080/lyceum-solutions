from flask import Flask, render_template, url_for

app = Flask(__name__)

PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
               'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
               'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']


@app.route('/login')
def login():
    params = {'emblem_url': url_for('static', filename='img/emblem.png')}
    return render_template('emergency_access.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
