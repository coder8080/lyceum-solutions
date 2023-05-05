import flask
from flask import jsonify
from . import db_session
from .job import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify({'jobs': jobs.to_dict()})
