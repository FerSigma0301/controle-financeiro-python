from flask import Flask

from app.models import db
from app.routes import bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI="sqlite:///finance.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
    return app
