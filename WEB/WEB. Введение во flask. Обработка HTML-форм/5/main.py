from flask import Flask, url_for

app = Flask(__name__)

main_page = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Отбор астронавтов</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="%%%PATH%%%" />
  </head>
  <body>
    <div class="d-flex flex-column align-items-center">
      <h1>Анкета претендента</h1>
      <h2>на участие в миссии</h2>
      <form class="p-3 rounded form border border-secondary">
        <div class="mb-3">
          <input
            type="text"
            class="form-control mb-1"
            placeholder="Введите фамилию"
          />
          <input
            type="text"
            class="form-control mb-2"
            placeholder="Введите имя"
          />
          <input
            type="email"
            class="form-control"
            placeholder="Введите адрес почты"
          />
        </div>
        <div class="mb-3">
          <label for="education">Какое у Вас образование?</label>
          <select name="" id="education" class="form-select">
            <option value="initial">Начальное</option>
            <option value="average">Среднее</option>
            <option value="higher">Высшее</option>
          </select>
        </div>
        <div class="mb-3">
          <p>Ваша профессия/профессии</p>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession1" />
            <label for="profession1">Инженер-исследователь</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession2" />
            <label for="profession2">Инженер-строитель</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession3" />
            <label for="profession3">Пилот</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession4" />
            <label for="profession4">Метеоролог</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession5" />
            <label for="profession5">Инженер по жизнеобеспечению</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession6" />
            <label for="profession6">Инженер по радиационной защите</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession7" />
            <label for="profession7">Врач</label>
          </div>
          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="profession8" />
            <label for="profession8">Экзобиолог</label>
          </div>
        </div>
        <div class="mb-3">
          <p>Укажите пол</p>
          <div class="form-check">
            <input
              type="text"
              class="form-check-input"
              type="radio"
              id="male"
            />
            <label for="male" class="form-check-label">Мужской</label>
          </div>
          <div class="form-check">
            <input
              type="text"
              class="form-check-input"
              type="radio"
              id="female"
            />
            <label for="female" class="form-check-label">Женский</label>
          </div>
        </div>
        <div class="mb-3">
          <label for="essay">Почему Вы хотитепринять участие в миссии?</label>
          <textarea name="" id="essay" rows="5" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="photo">Приложите Вашу фотографию</label>
          <input type="file" class="form-control" id="photo" />
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="ready-to-live" />
          <label for="ready-to-live" class="form-check-label"
            >Готовы остаться на Марсе?</label
          >
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
      </form>
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe"
      crossorigin="anonymous"
    ></script>
  </body>
</html>

"""


@app.route('/')
@app.route('/index')
def index():
    return main_page.replace('%%%PATH%%%', url_for('static', filename='css/main.css'))


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
