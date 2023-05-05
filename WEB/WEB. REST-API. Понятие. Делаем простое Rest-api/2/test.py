import requests

disclaimer_text = """
Перед запуском тестов убедитесь в том, что
1) Сервер запущен
2) В базе данных есть записи (если их нет, запустите скрипт add-data.py из корневой директории)
"""
print(disclaimer_text)


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
