"""
Модуль администратора сайта
"""
import os
from flask import render_template, Blueprint, request, url_for, redirect
from flask_login import current_user
from flask_website import app, db
from flask_website.auth_manager import UserRole
from flask_website.service import AdminService

siteadmin_blueprints = Blueprint(name='siteadmin', import_name=__name__, template_folder=os.path.join(app.config['TEMPLATE_FOLDER'], 'siteadmin'), url_prefix='/siteadmin')


def _require_authorized(func):
    def wrapper(*args, **kwargs):
        if current_user.get_user_role() != UserRole.administrator:
            return render_template("_401.html"), 401
        return func(*args, **kwargs)

    return wrapper


@_require_authorized
@siteadmin_blueprints.route("/", methods=["GET"])
def root():
    return render_template('main.html')


@_require_authorized
@siteadmin_blueprints.route("/profile", methods=["GET"])
def profile():
    adminService = current_user.get_control_object()
    return render_template('profile.html', admin=adminService.get_own_admin())


@_require_authorized
@siteadmin_blueprints.route("/profile", methods=["POST"])
def profilepush():
    newpass = request.form['newpass']
    adminService = current_user.get_control_object()
    adminService.change_password(newpass)
    return redirect(url_for('/siteadmin/profile'))


@_require_authorized
@siteadmin_blueprints.route("/contentmakermanagers", methods=["GET"])
def contentmakermanagerget():
    response_list = AdminService().get_all_contenmakers()
    return render_template('contentmakermanagers.html', contenmakers_list = response_list)


@_require_authorized
@siteadmin_blueprints.route("/contentmakermanagers", methods=["POST"])
def contentmakermanagerpush():
    login = request.form['login']
    mail = request.form['mail']
    AdminService().add_new_contentmacker(login, mail)
    return redirect(url_for('/siteadmin/contentmakermanagers'))


@_require_authorized
@siteadmin_blueprints.route("/contentmakermanagers", methods=["DELETE"])
def contentmakermanagerdel():
    id = request.form['id']
    AdminService().del_contentmaker(int(id))
    return redirect(url_for('/siteadmin/contentmakermanagers'))
