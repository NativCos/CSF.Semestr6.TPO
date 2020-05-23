"""
Модуль администратора сайта
"""
import os
from flask import render_template, Blueprint, request, url_for, redirect
from flask_login import current_user
from flask_login.mixins import AnonymousUserMixin
from flask_website import app, db
from flask_website.auth_manager import UserRole, FlaskUser
from flask_website.service import AdminService

siteadmin_blueprints = Blueprint(name='siteadmin', import_name=__name__, url_prefix='/siteadmin')


def _require_authorized():
    if not current_user.is_authenticated:
        return render_template("_401.html"), 401
    elif current_user.get_user_role() != UserRole.administrator:
        return render_template("_401.html"), 401
    else:
        return None


@siteadmin_blueprints.route("/", methods=["GET"])
def root():
    if _require_authorized() is not None:
        return _require_authorized()
    return render_template('/siteadmin/main.html')


@siteadmin_blueprints.route("/profile", methods=["GET"])
def profile():
    if _require_authorized() is not None:
        return _require_authorized()
    adminService = current_user.get_control_object()
    return render_template('/siteadmin/profile.html', login=adminService.get_own_admin().get_login())


@siteadmin_blueprints.route("/profile", methods=["POST"])
def profilepush():
    if _require_authorized() is not None:
        return _require_authorized()
    newpass = request.form['newpass']
    adminService = current_user.get_control_object()
    adminService.change_password(newpass)
    return redirect('/siteadmin/profile')


@siteadmin_blueprints.route("/contentmakermanagers", methods=["GET"])
def contentmakermanagerget():
    if _require_authorized() is not None:
        return _require_authorized()
    response_list = AdminService().get_all_contenmakers()
    return render_template('/siteadmin/contentmakermanagers.html', contenmakers_list = response_list)


@siteadmin_blueprints.route("/contentmakermanagers", methods=["POST"])
def contentmakermanagerpush():
    if _require_authorized() is not None:
        return _require_authorized()
    if request.form['action'] == 'create':
        login = request.form['login']
        mail = request.form['mail']
        AdminService().add_new_contentmacker(login, mail)
        return redirect('/siteadmin/contentmakermanagers')
    if request.form['action'] == 'delete':
        id = request.form['id']
        AdminService().del_contentmaker(int(id))
        return redirect('/siteadmin/contentmakermanagers')
    return render_template("_500.html"), 500
