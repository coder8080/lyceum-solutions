from flask import Flask, jsonify, url_for, render_template
import vk_api

app = Flask(__name__)

LOGIN: str = LOGIN
PASSWORD: str = PASSWORD


def custom_render(name: str, **params):
    style_url = url_for('static', filename='css/main.css')
    return render_template(name, **params, style_url=style_url)


@app.route('/vk_stat/<int:group_id>')
def vk_stat(group_id: int):
    session = vk_api.VkApi(
        LOGIN, PASSWORD
    )
    session.auth(token_only=True)

    user_vk = session.get_api()
    stats = user_vk.stats.get(group_id=group_id, intervals_count=10)
    likes_total = 0
    comments_total = 0
    subscribed_total = 0
    age_dict = dict()
    cities = set()
    for period in stats:
        if 'activity' in period:
            if 'likes' in period['activity']:
                likes_total += period['activity']['likes']
            if 'comments' in period['activity']:
                comments_total += period['activity']['comments']
            if 'subscribed' in period['activity']:
                subscribed_total += period['activity']['subscribed']
        if 'reach' in period and 'age' in period['reach']:
            for age in period['reach']['age']:
                count = age['count']
                value = age['value']
                if value not in age_dict:
                    age_dict[value] = 0
                age_dict[value] += count
            if 'cities' in period['reach']:
                for city in period['reach']['cities']:
                    cities.add(city['name'])
    age_list = list(age_dict.items())
    age_list.sort()
    params = {'likes_total': likes_total, 'comments_total': comments_total,
              'subscribed_total': subscribed_total, 'age_list': age_list, 'cities': cities}
    return custom_render('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
