import requests

response = requests.put('http://localhost:8080/api/jobs/1',
                        json={'team_leader_id': 1, 'job': 'add new job', 'work_size': 15, 'is_finished': False, 'collaborators': '2, 3'}).json()
print(response)
