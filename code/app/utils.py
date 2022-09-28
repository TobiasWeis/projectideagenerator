import requests
from datetime import date
import json
from .data import actors, actions, objects, technologies, industries


def GetRowVals(row, exclude=["password"], full_datetime=False):
    """
    Get all column values of a row in a database
    args: row from database
    returns: dict of column names to column values for that row of database
    """
    row_vals = {}
    for k, v in row.__dict__.items():
        if not k.startswith("_") and not k in exclude:
            if isinstance(v, date) and not full_datetime:
                row_vals[k] = v.strftime("%Y-%m-%d")
            else:
                row_vals[k] = v
    return row_vals


def seed_data(db, models):
    if models.Actor.query.first() is None:
        for a in actors:
            db.session.add(models.Actor(name=a))
        db.session.commit()

    if models.Action.query.first() is None:
        for a in actions:
            db.session.add(models.Action(name=a))
        db.session.commit()

    if models.Object.query.first() is None:
        for o in objects:
            db.session.add(models.Object(name=o))
        db.session.commit()
        
    if models.Technology.query.first() is None:
        for t in technologies:
            db.session.add(models.Technology(name=t))
        db.session.commit()

    if models.Industry.query.first() is None:
        for i in industries:
            db.session.add(models.Industry(name=i))
        db.session.commit()

    if models.Idea.query.first() is None:
        db.session.add(models.Idea(name="Irgendeine Schwachsinns-Idee von Tobi"))
        db.session.commit()
