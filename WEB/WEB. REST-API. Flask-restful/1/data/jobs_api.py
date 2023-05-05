import flask
from flask import jsonify, request, make_response
from . import db_session
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify({'jobs': [job.to_dict() for job in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id: int):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify({'jobs': jobs.to_dict()})


@blueprint.route('/api/jobs/<job_id>')
def get_job_error(job_id: str):
    return jsonify({'error': 'Bad request'}), 401


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return make_response(jsonify({"error": 'Empty request'}), 400)
    elif not all(list(key in request.json for key in ['team_leader_id', 'job', 'work_size', 'collaborators', 'is_finished'])):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    session = db_session.create_session()
    job = Job(team_leader=request.json['team_leader_id'], job=request.json['job'], work_size=int(
        request.json['work_size']), collaborators=request.json['collaborators'], is_finished=request.json['is_finished'])
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id: int):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 400)
    session.delete(job)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id: int):
    sesion = db_session.create_session()
    job = sesion.query(Job).filter(Job.id == job_id).first()
    if not job:
        return make_response(jsonify({"error": 'Not found'}), 400)
    elif not request.json:
        return make_response(jsonify({"error": 'Empty request'}), 400)
    elif not all(list(key in request.json for key in ['team_leader_id', 'job', 'work_size', 'collaborators', 'is_finished'])):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    job.team_leader = request.json['team_leader_id']
    job.job = request.json['job']
    job.work_size = int(request.json['work_size'])
    job.collaborators = request.json['collaborators']
    job.is_finished = request.json['is_finished']
    sesion.commit()
    return jsonify({'success': 'OK'})
