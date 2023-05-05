from .users import User
from . import db_session
from flask import jsonify, make_response
from flask_restful import abort, reqparse, Resource
from flask_login import current_user

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)


def abort_if_not_found(user_id: int):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f'User {user_id} not found')
        return


class UsersResource(Resource):
    def get(self, user_id: int):
        abort_if_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict()})

    def delete(self, user_id: int):
        abort_if_not_found(user_id)
        if not current_user.is_authenticated or user_id != current_user.id:
            return make_response(jsonify({'error': 'Not allowed'}), 403)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        session.delete(users)
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [user.to_dict(only=['name', 'surname']) for user in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(surname=args['surname'], name=args['name'], age=args['age'],
                    position=args['position'], speciality=args['speciality'],
                    address=args['address'], email=args['email'], hashed_password=args['hashed_password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
