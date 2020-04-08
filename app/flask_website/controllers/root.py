from flask import render_template, Blueprint, request

from flask_website import app, db


root_blueprints = Blueprint('root', __name__, template_folder=app.config['TEMPLATE_FOLDER'])


@root_blueprints.route("/", methods=["GET"])
def root():
    return "..."


@root_blueprints.route("/history", methods=["GET"])
@root_blueprints.route("/contacts", methods=["GET"])
@root_blueprints.route("/team", methods=["GET"])
@root_blueprints.route("/matches", methods=["GET"])
@root_blueprints.route("/news", methods=["GET"])
@root_blueprints.route("/news/<int:id>", methods=["GET"])


@root_blueprints.errorhandler(404)
def page_not_found(e):
    return render_template('_404.html'), 404
