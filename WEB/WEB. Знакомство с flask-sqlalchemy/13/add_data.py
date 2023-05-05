from data import db_session
from data.users import User
from data.jobs import Job
import datetime


db_session.global_init('db/database.db')
session = db_session.create_session()

captain = User()
captain.surname = 'Scott'
captain.name = 'Ridley'
captain.age = 21
captain.position = 'captain'
captain.speciality = 'research engineer'
captain.address = 'module_1'
captain.email = 'scott_chief@mars.org'

user1 = User()
user1.surname = 'Леонов'
user1.name = 'Артём'
user1.age = 23
user1.position = 'помошник капитана'
user1.speciality = 'инженер - строитель'
user1.address = 'module_2'
user1.email = 'leonov@mars.org'


user2 = User()
user2.surname = 'Харитонов'
user2.name = 'Артём'
user2.age = 19
user2.position = 'старший специалист'
user2.speciality = 'экзобиолог'
user2.address = 'module_3'
user2.email = 'haritonov@mars.org'

user3 = User()
user3.surname = 'Бессонов'
user3.name = 'Сергей'
user3.age = 20
user3.position = 'младший специалист'
user3.speciality = 'инженер по жизнеобеспечению'
user3.address = 'module_4'
user3.email = 'bessonov@mars.org'

job1 = Job()
job1.team_leader = 1
job1.job = 'deployment of residential modules 1 and 2'
job1.work_size = 15
job1.collaborators = '2, 3'
start_date = datetime.datetime.now()
job1.is_finished = False

session.add(captain)
session.add(user1)
session.add(user2)
session.add(user3)
session.add(job1)
session.commit()
