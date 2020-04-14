import os
from flask import render_template, Blueprint, request, url_for, redirect

from flask_website import app, db


siteadmin_blueprints = Blueprint(name='siteadmin', import_name=__name__, template_folder=os.path.join(app.config['TEMPLATE_FOLDER'], 'siteadmin'), url_prefix='/siteadmin')


@siteadmin_blueprints.route("/", methods=["GET"])
def root():
    return render_template('main.html')


@siteadmin_blueprints.route("/profile", methods=["GET"])
def profile():
    return render_template('profile.html')


@siteadmin_blueprints.route("/profile", methods=["PUSH"])
def profilepush():
    newpass = request.form['newpass']
    return redirect(url_for('/siteadmin/profile'))


@siteadmin_blueprints.route("/contentmakermanager", methods=["GET"])
def contentmakermanagerget():
    return render_template('contentmakermanager.html')


@siteadmin_blueprints.route("/contentmakermanager", methods=["PUSH"])
def contentmakermanagerpush():
    name = request.form['name']
    mail = request.form['mail']
    return redirect(url_for('/siteadmin/contentmakermanager'))


@siteadmin_blueprints.route("/contentmakermanager", methods=["DELETE"])
def contentmakermanagerdel():
    id = request.form['id']
    return redirect(url_for('/siteadmin/contentmakermanager'))
