from flask import Blueprint, jsonify, request
from flask import render_template
import datetime

from sqlalchemy import and_

from app import db

pages_blueprint = Blueprint('pages_blueprint', __name__, url_prefix="", template_folder='../templates/', static_folder='static', static_url_path='../static/')

@pages_blueprint.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@pages_blueprint.route('/settings', methods=['GET'])
def page2():
    return render_template('settings.html')
