from flask import Flask


def create_app():
    # create Flask app instance
    app = Flask(__name__)

    # Register Blueprints
    from .routes import blueprint

    app.register_blueprint(blueprint)

    return app
