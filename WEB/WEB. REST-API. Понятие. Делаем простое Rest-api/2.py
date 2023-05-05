import flask
from flask import jsonify
from . import db_session
from .job import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs/<int:job_id>')
def get_news(job_id: int):
    session = db_session.create_session()
    jobs = session.query(Job).filter(Job.id == job_id)
    return jsonify({'jobs': jobs.to_dict()})
