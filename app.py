import os.path
from flask import Flask, redirect, url_for, logging
from flask_sqlalchemy import SQLAlchemy
from logging import Formatter
from database import db_session
from app_factory import create_app

app = create_app()

@app.route('/')
def index():
    app.logger.debug(app.url_map)
    return redirect(url_for('slt.index'))
    
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()