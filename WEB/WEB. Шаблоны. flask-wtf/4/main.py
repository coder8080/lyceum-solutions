from flask import Flask, render_template, url_for

app = Flask(__name__)

PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
               'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
               'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']


@app.route('/answer')
def answer():
    params = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего', 'professoin': 'штурман марсохода',
              'gender': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': True, 'style_url': url_for('static', filename='css/main.css')}
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
