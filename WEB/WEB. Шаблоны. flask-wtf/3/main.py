from flask import Flask, render_template, request, url_for

app = Flask(__name__)

PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
               'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
               'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']


@app.route('/list_prof/<type>')
def list_prof(type: str):
    params = {'type': type, 'professions': PROFESSIONS}
    return render_template('list_prof.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
