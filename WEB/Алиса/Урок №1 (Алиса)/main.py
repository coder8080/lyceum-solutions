from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

sessionStorage = {}
second_stage = set()


@app.route('/post', methods=['POST'])
def post():
    logging.info(f'Request: {request.json!r}')
    response = {'session': request.json['session'],
                'version': request.json['version'], 'response': {'end_session': False}}
    handle_dialog(request.json, response)
    logging.info(f'Response: {response!r}')
    return jsonify(response)


def handle_dialog(req: dict, res: dict):
    user_id = str(req['session']['user_id'])
    if req['session']['new'] or user_id not in sessionStorage:
        # Новый пользователь
        sessionStorage[user_id] = {
            'suggests': ['Не хочу.!', 'Не буду.', 'Отстань!'], 'stage': 1 if user_id not in second_stage else 2}
        if user_id not in second_stage:
            res['response']['text'] = 'Привет! Купи слона!'
            res['response']['buttons'] = get_suggests(user_id)
            return
    if req['request']['original_utterance'].lower() in ['ладно', 'куплю', 'хорошо', 'покупаю', 'я покупаю', 'я куплю']:
        if sessionStorage[user_id]['stage'] == 1:
            # Пользователь согласился купить слона
            res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!\nКупи кролика!'
            res['response']['end_session'] = False
            del sessionStorage[user_id]
            second_stage.add(user_id)
        else:
            # Пользователь согласился купить кролика
            res['response']['text'] = 'Кролика можно найти на Яндекс.Маркете!'
            res['response']['end_session'] = True
            del sessionStorage[user_id]
            second_stage.remove(user_id)
        return
    t = ""
    if sessionStorage[user_id]['stage'] == 1:
        t = f'Все говорят "{req["request"]["original_utterance"]}", а ты купи слона!'
    else:
        t = f'Все говорят "{req["request"]["original_utterance"]}", а ты купи кролика!'
    res['response']['text'] = t
    res['response']['buttons'] = get_suggests(user_id)


def get_suggests(user_id):
    session = sessionStorage[user_id]
    suggests = [{'title': suggest, 'hide': True}
                for suggest in session['suggests'][:2]]
    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    if len(suggests) < 2:
        suggests.append(
            {'title': 'Ладно', 'url': f'https://market.yandex.ru/search?text={ "слон" if sessionStorage[user_id]["stage"] == 1 else "кролик"}', 'hide': True})

    return suggests


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
