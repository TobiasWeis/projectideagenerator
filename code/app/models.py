from . import db
from sqlalchemy import event
import uuid
import datetime
from flask import current_app


def create_log_message(startstring, target):
    """
    Creates log-messages that contain the table/object-name and it's attributes and values
    """
    string = f"{startstring} {target.__class__.__name__}: "
    for k, v in target.__dict__.items():
        if k not in ["password", "id", "_sa_instance_state"]:
            string += f"{k}:{v}, "

    current_app.logger.debug(string)

    return string


class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Action(db.Model):
    __tablename__ = 'action'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Object(db.Model):
    __tablename__ = 'objects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Technology(db.Model):
    __tablename__ = 'technology'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Industry(db.Model):
    __tablename__ = 'industry'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Idea(db.Model):
    __tablename__ = 'idea'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
