from flask import Blueprint, jsonify, request, abort
from flask import render_template
import re, html
import datetime
import random

from sqlalchemy import and_

from app import db
from app.models import * 
from app.utils import GetRowVals

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix="/api", template_folder='../templates/', static_folder='static', static_url_path='../static/')

def sanitize(text):
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

    # Remove well-formed tags, fixing mistakes by legitimate users
    no_tags = tag_re.sub('', text)

    # Clean up anything else by escaping
    ready_for_web = html.escape(no_tags)

    return ready_for_web


@api_blueprint.route('/version', methods=['POST'])
def version():
    return jsonfiy({"version":0.1})

@api_blueprint.route('/random', methods=['GET'])
def get_random():
    actor = random.choice(Actor.query.all()).name
    action = random.choice(Action.query.all()).name
    obj = random.choice(Object.query.all()).name
    technology = random.choice(Technology.query.all()).name
    industry = random.choice(Industry.query.all()).name
    
    return f"{actor} that {action} {obj} by using {technology} (in the industry of {industry})"

#--- get lists

@api_blueprint.route('/actor', methods=['GET'])
def get_actors():
    rc = []
    for a in Actor.query.all():
        rc.append(GetRowVals(a))
    return jsonify(rc)

@api_blueprint.route('/action', methods=['GET'])
def get_actions():
    rc = []
    for a in Action.query.all():
        rc.append(GetRowVals(a))
    return jsonify(rc)

@api_blueprint.route('/object', methods=['GET'])
def get_objects():
    rc = []
    for a in Object.query.all():
        rc.append(GetRowVals(a))
    return jsonify(rc)

@api_blueprint.route('/technology', methods=['GET'])
def get_technologies():
    rc = []
    for a in Technology.query.all():
        rc.append(GetRowVals(a))
    return jsonify(rc)

@api_blueprint.route('/industry', methods=['GET'])
def get_industries():
    rc = []
    for a in Industry.query.all():
        rc.append(GetRowVals(a))
    return jsonify(rc)

@api_blueprint.route('/idea', methods=['GET'])
def get_ideas():
    rc = []
    for i in Idea.query.all():
        rc.append(GetRowVals(i))
    return jsonify(rc)

#--- CRUD Operations (insert, delete)

# actor
@api_blueprint.route('/actor/<int:id>', methods=['DELETE'])
def delete_actor(id):
    actor = Actor.query.get(id)
    if actor is None:
        abort(404)
    db.session.delete(actor)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/actor', methods=['POST'])
def insert_actor():
    if not request.json: abort(400)

    actor = Actor(name=sanitize(request.json.get('name')))
    db.session.add(actor)
    db.session.commit()

    return jsonify({'result': True})

# action
@api_blueprint.route('/action/<int:id>', methods=['DELETE'])
def delete_action(id):
    action = Action.query.get(id)
    if action is None:
        abort(404)
    db.session.delete(action)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/action', methods=['POST'])
def insert_action():
    if not request.json: abort(400)

    action = Action(name=sanitize(request.json.get('name')))
    db.session.add(action)
    db.session.commit()

    return jsonify({'result': True})

# object
@api_blueprint.route('/object/<int:id>', methods=['DELETE'])
def delete_object(id):
    obj = Object.query.get(id)
    if obj is None:
        abort(404)
    db.session.delete(obj)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/object', methods=['POST'])
def insert_object():
    if not request.json: abort(400)

    obj = Object(name=sanitize(request.json.get('name')))
    db.session.add(obj)
    db.session.commit()

    return jsonify({'result': True})


# technology
@api_blueprint.route('/technology/<int:id>', methods=['DELETE'])
def delete_technology(id):
    technology = Technology.query.get(id)
    if technology is None:
        abort(404)
    db.session.delete(technology)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/technology', methods=['POST'])
def insert_technology():
    if not request.json: abort(400)

    technology = Technology(name=sanitize(request.json.get('name')))
    db.session.add(technology)
    db.session.commit()

    return jsonify({'result': True})

# Industry

@api_blueprint.route('/industry/<int:id>', methods=['DELETE'])
def delete_industry(id):
    industry = Industry.query.get(id)
    if industry is None:
        abort(404)
    db.session.delete(industry)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/industry', methods=['POST'])
def insert_industry():
    if not request.json: abort(400)

    industry = Industry(name=sanitize(request.json.get('name')))
    db.session.add(industry)
    db.session.commit()

    return jsonify({'result': True})

# Idea

@api_blueprint.route('/idea/<int:id>', methods=['DELETE'])
def delete_idea(id):
    idea = Idea.query.get(id)
    if idea is None:
        abort(404)
    db.session.delete(idea)
    db.session.commit()

    return jsonify({'result': True})

@api_blueprint.route('/idea', methods=['POST'])
def insert_idea():
    if not request.json: abort(400)

    idea = Idea(name=sanitize(request.json.get('name')))
    db.session.add(idea)
    db.session.commit()

    return jsonify({'result': True})

