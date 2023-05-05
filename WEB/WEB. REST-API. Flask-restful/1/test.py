import requests


print('ℹ️ Запускаю тесты модулей')
print('ℹ️ Запускаю тесты user_resource.py')

# Корректное создание пользователя
response = requests.post('http://localhost:8080/api/v2/users',
                         json={'surname': 'Morales', 'name': 'Miles',
                               'age': '16', 'position': 'student',
                               'speciality': 'The only spider-man of New York',
                               'address': 'Earth-1610', 'email': 'spiderman@marvel.com',
                               'hashed_password': 'c9344c5f1079f7ce9b007e604829f7e8e4516e9132e098ebd58e2cc7f2a5fd4c'}).json()
assert 'success' in response
assert response['success'] == 'OK'
print('✅ Корректное создание пользователя')

# Ошибка при создании пользователя с повторяющейся почтой
response = requests.post('http://localhost:8080/api/v2/users',
                         json={'surname': 'Morales', 'name': 'Miles',
                               'age': '16', 'position': 'student',
                               'speciality': 'The only spider-man of New York',
                               'address': 'Earth-1610', 'email': 'spiderman@marvel.com',
                               'hashed_password': 'c9344c5f1079f7ce9b007e604829f7e8e4516e9132e098ebd58e2cc7f2a5fd4c'})
assert response.status_code == 500
print('✅ Ошибка при создании пользователя с повторяющейся почтой')

# Ошибка при создании пользователя с пустыми параметрами
response = requests.post('http://localhost:8080/api/v2/users', json={})
assert response.status_code == 400
print('✅ Ошибка при создании пользователя с пустыми параметрами')

# Получение пользователя по id
response = requests.get('http://localhost:8080/api/v2/users/1').json()
assert 'users' in response
print('✅ Получение пользователя по id')

# Получение всех пользователей
response = requests.get('http://localhost:8080/api/v2/users').json()
assert 'users' in response
assert len(response['users']) >= 1
print('✅ Получение всех пользователей')

print()
print('ℹ️ Запускаю тесты jobs_resource.py')
# Корректное создание задачи
response = requests.post('http://localhost:8080/api/v2/jobs',
                         json={'team_leader': 1, 'job': 'add new job',
                               'work_size': 15, 'is_finished': False,
                               'collaborators': '2, 3'}).json()
assert 'success' in response
assert response['success'] == 'OK'
print('✅ Корректное создание задачи')

# Ошибка при создании задачи без аргументов
response = requests.post('http://localhost:8080/api/v2/jobs',
                         json={}).json()
assert 'message' in response
print('✅ Ошибка при создании задачи без аргументов')

print()
print('ℹ️ Запускаю тесты первой версии API')

# ---
response = requests.get('http://localhost:8080/api/jobs').json()
assert 'jobs' in response
assert len(response['jobs']) >= 1
print('✅ Получение всех задач')

# ---
response = requests.get('http://localhost:8080/api/jobs/1').json()
assert 'jobs' in response
assert 'id' in response['jobs']
print('✅ Получение одной задачи')

# ---
response = requests.get('http://localhost:8080/api/jobs/100500').json()
assert 'error' in response
assert response['error'] == 'Not found'
print('✅ Ошибка при неверном id')

# ---
response = requests.get('http://localhost:8080/api/jobs/asdf').json()
assert 'error' in response
assert response['error'] == 'Bad request'
print('✅ Ошибка при неправильном типе id')


# ---
response = requests.post('http://localhost:8080/api/jobs',
                         json={'team_leader_id': 1, 'job': 'add new job', 'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'success' in response
assert response['success'] == 'OK'
print('✅ Добавление корректной задачи')

# ---
response = requests.post('http://localhost:8080/api/jobs',
                         json={}).json()
assert 'error' in response
assert response['error'] == 'Empty request'
print('✅ Ошибка при пустом запросе [Добавление задачи]')

# ---
response = requests.post('http://localhost:8080/api/jobs',
                         json={'job': 'add new job', 'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'error' in response
assert response['error'] == 'Bad request'
print('✅ Ошибка при отсутствии поля team_leader [Добавление задачи]')

# ---
response = requests.post('http://localhost:8080/api/jobs',
                         json={'team_leader_id': 1,  'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'error' in response
assert response['error'] == 'Bad request'
print('✅ Ошибка при отсутствии поля job [Добавление задачи]')


# ---
response = requests.put('http://localhost:8080/api/jobs/1',
                        json={'team_leader_id': 1, 'job': 'edited job', 'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'success' in response
assert response['success'] == 'OK'
response = requests.get('http://localhost:8080/api/jobs/1').json()
assert 'jobs' in response
assert response['jobs']['job'] == 'edited job'
print('✅ Изменение задачи')

# ---
response = requests.put('http://localhost:8080/api/jobs/1',
                        json={'job': 'add new job', 'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'error' in response
assert response['error'] == 'Bad request'
print('✅ Ошибка при отсутствии поля team_leader [Изменение задачи]')

# ---
response = requests.put('http://localhost:8080/api/jobs/1',
                        json={'team_leader_id': 1,  'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
assert 'error' in response
assert response['error'] == 'Bad request'
print('✅ Ошибка при отсутствии поля job [Изменение задачи]')


# ---
response = requests.delete('http://localhost:8080/api/jobs/1',
                           ).json()
assert 'success' in response
assert response['success'] == 'OK'
response = requests.get('http://localhost:8080/api/jobs/1').json()
assert 'error' in response
assert response['error'] == 'Not found'
print('✅ Удаление задачи')

print()
print('📗 Тесты прошли успешно')
