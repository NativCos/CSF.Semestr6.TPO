"""
Модуль Клиента
"""
from datetime import datetime

from flask import render_template, Blueprint, request, redirect, url_for
from sqlalchemy import desc

from flask_website import app, db
from flask_website.auth_manager import FlaskUser, UserRole
from flask_website.models import Game_match, News
from flask_website.service import ClientService
from flask_login import current_user, login_user, logout_user, login_required

root_blueprints = Blueprint('root', __name__, template_folder=app.config['TEMPLATE_FOLDER'])


def get_first_future_match():
    future_matches = db.session.query(Game_match).filter(Game_match.score_own == 999).order_by(Game_match.date)
    future_match = {}
    future_match['rival'] = future_matches.first().rival
    future_match['date_place'] = str(future_matches[0].date.strftime('%c')) + ' ' + future_matches[0].place_of_play
    return future_match


def get_micro_mews(limit: int = 3):
    if limit == 0:
        news_raw = News.query.order_by(News.date).all()
    else:
        news_raw = db.session.query(News).order_by(News.date).limit(limit).all()
    news = []
    for i in range(len(news_raw)):
        news.append({
        'id': news_raw[i].id,
        'date': news_raw[i].date.strftime('%c'),
        'header': news_raw[i].header,
        'micro_body': news_raw[i].body[:100:]})
    return news


@app.errorhandler(404)
def page_not_found(e):
    return render_template('_404.html'), 404


@root_blueprints.route("/", methods=["GET"])
def root():
    lastgames = db.session.query(Game_match).filter(Game_match.score_own != 999).order_by(Game_match.date).limit(3)
    return render_template("index.html", lastgames=lastgames, micronews=get_micro_mews(),
                           future_match=get_first_future_match())


@root_blueprints.route("/history", methods=["GET"])
def history():
    return render_template("history.html")


@root_blueprints.route("/contacts", methods=["GET"])
def contacts():
    return render_template("contacts.html")


@root_blueprints.route("/team", methods=["GET"])
def team():
    return render_template("team.html", future_match=get_first_future_match())


@root_blueprints.route("/matches", methods=["GET"])
def matches():
    matchs_raw = db.session.query(Game_match).order_by(desc(Game_match.date))
    return render_template("matches.html", matchs=matchs_raw, future_match=get_first_future_match())

@root_blueprints.route("/news", methods=["GET"])
def news():
    return render_template("news.html", micronews=get_micro_mews(0), future_match=get_first_future_match())

@root_blueprints.route("/news/<int:id>", methods=["GET"])
def thenews(id):
    response_news = ClientService.get_thenews(id)
    return render_template("thenews.html", news=response_news, future_match=get_first_future_match())

@root_blueprints.route("/login", methods=["GET"])
def loginget():
    if current_user.is_authenticated:
        if current_user.get_user_role() == UserRole.administrator:
            return redirect('/siteadmin')
        elif current_user.get_user_role() == UserRole.contentmaker:
            return redirect('/contentmaker')
    return render_template('login.html')

@root_blueprints.route("/login", methods=["POST"])
def loginpost():
    login = request.form['login']
    password = request.form['password']
    FlaskUser.login(login, password)
    return redirect('/login')

@root_blueprints.route("/logout", methods=["GET"])
def logout():
    if logout_user():
        return redirect('/login')
    return render_template('_500.html'), 500
