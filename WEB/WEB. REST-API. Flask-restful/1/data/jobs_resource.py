from .jobs_parser import parser
from .db_session import create_session
from .jobs import Job
from flask_restful import abort, Resource
from flask import jsonify, make_response
from flask_login import current_user


def abort_if_not_found(job_id: int):
    session = create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        abort(404, message=f'Job {job_id} not found')
        return


class JobsResource(Resource):
    def get(self, job_id: int):
        abort_if_not_found(job_id)
        session = create_session()
        jobs = session.query(Job).get(job_id)
        return jsonify({'jobs': jobs.to_dict()})

    def delete(self, job_id: int):
        abort_if_not_found(job_id)
        session = create_session()
        jobs = session.query(Job).get(job_id)
        if not current_user.is_authenticated or not (current_user.id == 1 or current_user.id == jobs.team_leader):
            return abort(403, message=f'Not enough privileges')
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = create_session()
        jobs = session.query(Job).all()
        return jsonify({'jobs': [job.to_dict() for job in jobs]})

    def post(self):
        args = parser.parse_args()
        session = create_session()
        job = Job(team_leader=args['team_leader'], job=args['job'], work_size=args['work_size'],
                  collaborators=args['collaborators'], is_finished=bool(args['is_finished']))
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
