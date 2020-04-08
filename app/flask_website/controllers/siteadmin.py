import os
from flask import render_template, Blueprint, request

from flask_website import app, db


siteadmin_blueprints = Blueprint(name='siteadmin', import_name=__name__, template_folder=os.path.join(app.config['TEMPLATE_FOLDER'], 'siteadmin'), url_prefix='siteadmin')


@siteadmin_blueprints.route("/", methods=["GET"])
def root():
    return "..."
