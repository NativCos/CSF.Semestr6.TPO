from flask import render_template, Blueprint, request

from flask_website import app, db

root_blueprints = Blueprint('root', __name__, template_folder=app.config['TEMPLATE_FOLDER'])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('_404.html'), 404


@root_blueprints.route("/", methods=["GET"])
def root():
    return render_template("index.html")


@root_blueprints.route("/history", methods=["GET"])
def history():
    return render_template("history.html")


@root_blueprints.route("/contacts", methods=["GET"])
def contacts():
    return render_template("contacts.html")


@root_blueprints.route("/team", methods=["GET"])
def team():
    return render_template("team.html")


@root_blueprints.route("/matches", methods=["GET"])
def matches():
    st = request.form['st']
    return render_template("matches.html")


@root_blueprints.route("/news", methods=["GET"])
def news():
    st = request.form['st']
    return render_template("news.html")


@root_blueprints.route("/news/<int:id>", methods=["GET"])
def thenews(id):
    return render_template("thenews.html")

