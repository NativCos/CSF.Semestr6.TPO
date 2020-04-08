import os
from flask import render_template, Blueprint, request

from flask_website import app, db


contentmaker_blueprints = Blueprint('contentmaker', __name__, os.path.join(template_folder=app.config['TEMPLATE_FOLDER']), 'contentmaker')


@contentmaker_blueprints.route("/", methods=["GET"])
def root():
    return "..."
