from flask import render_template
from . import main
from app.request_handler import get_news_sources, get_articles

@main.route("/")
def index():
    sources=get_news_sources()
    return render_template("./index.html",sources=sources)

@main.route("/articles/<string:source_id>")
def articles(source_id):
    articles=get_articles(source_id)
    return render_template("./articles.html",articles=articles)
