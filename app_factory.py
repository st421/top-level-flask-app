import os.path
from flask import Flask, logging
from logging import Formatter

def create_app(config_file=None):
    app = Flask(__name__)
    init_logging(app)

    from slt.slt import slt
    from ca.ca import ca
    app.register_blueprint(slt, url_prefix='/slt')
    app.register_blueprint(ca, url_prefix='/chronicling-america')

    return app

def init_logging(app):
    h = logging.StreamHandler()
    h.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(h)
    app.logger.setLevel(logging.DEBUG)