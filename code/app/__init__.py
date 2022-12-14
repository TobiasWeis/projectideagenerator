from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from flask_apscheduler import APScheduler
from apscheduler.jobstores.base import ConflictingIdError
from apscheduler.schedulers import SchedulerAlreadyRunningError
import atexit

from .db_extensions import db
from .utils import *

scheduler = APScheduler()

def periodic_function():
    """
    Functionalities that should be executed periodically on a schedule
    """
    pass

def create_app():
    from . import models
    from .views.pages import pages_blueprint
    from .views.api import api_blueprint

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')

    CORS(app)

    db.init_app(app)

    app.register_blueprint(pages_blueprint)
    app.register_blueprint(api_blueprint)


    with app.app_context():
        db.create_all()
        seed_data(db, models)

        Swagger(app)

        if False: # set to true and configure if you want periodic tasks
            try:
                # get the current checkins every minute
                scheduler.add_job(id=f"checkins for {c}",
                                  func=periodic_function,
                                  trigger='cron',
                                  minute='*/1',
                                  hour='*',
                                  misfire_grace_time=30)

            except ConflictingIdError:
                print("ERROR: Schedule job was already there")
                pass

            try:
                scheduler.init_app(app)
                scheduler.start()
                atexit.register(lambda:scheduler.shutdown())
            except SchedulerAlreadyRunningError:
                print("ERROR: Scheduler already running")

        return app
