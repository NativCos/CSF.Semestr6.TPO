"""
Модуль Клиента
"""
from flask import render_template, Blueprint, request, redirect, url_for
from flask_website import app, db
from flask_website.auth_manager import FlaskUser, UserRole
from flask_website.service import ClientService
from flask_login import current_user, login_user, logout_user, login_required

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
    response_list_matches = ClientService.get_all_matches()
    return render_template("matches.html", response_list_matches=response_list_matches)


@root_blueprints.route("/news", methods=["GET"])
def news():
    response_list_news = ClientService.get_all_news()
    return render_template("news.html", response_list_news=response_list_news)


@root_blueprints.route("/news/<int:id>", methods=["GET"])
def thenews(id):
    response_news = ClientService.get_thenews(id)
    return render_template("thenews.html", response_news=response_news)


@root_blueprints.route("/login", methods=["GET"])
def loginget():
    if current_user.is_authenticated:
        if current_user.get_user_role() == UserRole.administrator:
            return redirect(url_for('/contentmaker'))
        elif current_user.get_user_role() == UserRole.contentmaker:
            return redirect(url_for('/siteadmin'))
    return render_template('login.html')


@root_blueprints.route("/login", methods=["POST"])
def loginpost():
    login = request.form['login']
    password = request.form['password']
    FlaskUser.login(login, password)
    redirect(url_for('/login'))


@root_blueprints.route("/logout", methods=["GET"])
def logout():
    if logout_user():
        return redirect(url_for('/'))
    return render_template('_500.html'), 500
