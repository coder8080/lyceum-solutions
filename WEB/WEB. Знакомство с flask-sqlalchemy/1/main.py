
from sqlalchemy.orm import Session


def global_init(db_name: str):
    return


def create_session() -> Session:
    return


class User:
    pass


db_name = input()

global_init(db_name)
session = create_session()

for user in session.query(User).filter(User.position.notlike('%engineer%'),
                                       User.speciality.notlike('%engineer%'),
                                       User.address == 'module_1'):
    print(user.id)
