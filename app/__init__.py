from flask import Flask,render_template
from flask_bootstrap import Bootstrap

def create_app():
    app=Flask(__name__)
    Bootstrap(app)
    from app.main import main
    app.register_blueprint(main)
    return app
