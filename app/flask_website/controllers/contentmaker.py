"""
Модуль контент мейкера
"""
import os
from datetime import datetime
from flask import render_template, Blueprint, request, url_for, redirect
from flask_login import current_user
from flask_website import app, db
from flask_website.service import ContentmakerService
from flask_website.auth_manager import UserRole

contentmaker_blueprints = Blueprint(name='contentmaker', import_name=__name__,
                                    template_folder=os.path.join(app.config['TEMPLATE_FOLDER'], 'contentmaker'),
                                    url_prefix='/contentmaker')


def _require_authorized(func):
    def wrapper(*args, **kwargs):
        if current_user.get_user_role() != UserRole.contentmaker:
            return render_template("_401.html"), 401
        return func(*args, **kwargs)

    return wrapper


@_require_authorized
@contentmaker_blueprints.route("/", methods=["GET"])
def root():
    return render_template("main.html")


@_require_authorized
@contentmaker_blueprints.route("/news", methods=["GET"])
def news():
    response_list_news = ContentmakerService.get_all_news()
    return render_template("news.html", response_list_news=response_list_news)


@_require_authorized
@contentmaker_blueprints.route("/news/new", methods=["GET"])
def newnews():\
    return render_template("editthenews.html")


@_require_authorized
@contentmaker_blueprints.route("/news/new", methods=["POST"])
def editnewspush():
    header = request.form['header']
    body = request.form['body']
    date = request.form['date']
    ContentmakerService.add_new_news(header, body, datetime.strptime(date, "%Y-%m-%d"))  # ?
    return redirect(url_for('/contentmaker/news'))


@_require_authorized
@contentmaker_blueprints.route("/news", methods=["DELETE"])
def delnews():
    id = request.form['id']
    ContentmakerService.del_news(int(id))
    return redirect(url_for('/contentmaker/news'))


@_require_authorized
@contentmaker_blueprints.route("/matches", methods=["GET"])
def matches():
    response_list_matches = ContentmakerService.get_all_matches()
    return render_template("matches.html", response_list_matches=response_list_matches)


@_require_authorized
@contentmaker_blueprints.route("/matches/new", methods=["GET"])
def newmatches():
    return render_template("newthematche.html")


@_require_authorized
@contentmaker_blueprints.route("/matches/new", methods=["POST"])
def newmatchespush():
    date = request.form['date']
    score_own = request.form['score_own']
    score_rival = request.form['score_rival']
    rival = request.form['rival']
    place_of_play = request.form['place_of_play']
    ContentmakerService.add_new_match(datetime.strptime(date, "%Y-%m-%d"), int(score_own), int(score_rival), rival,
                                      place_of_play)
    return redirect(url_for('/contentmaker/matches'))


@_require_authorized
@contentmaker_blueprints.route("/matches/change", methods=["GET"])
def editmatches():
    id = request.form['id']
    match = ContentmakerService.get_thematch(int(id))
    return render_template("editthematche.html", match=match)


@_require_authorized
@contentmaker_blueprints.route("/matches/change", methods=["POST"])
def editmatchespush():
    id = request.form['id']
    date = request.form['date']
    score_own = request.form['score_own']
    score_rival = request.form['score_rival']
    rival = request.form['rival']
    place_of_play = request.form['place_of_play']
    ContentmakerService.ch_match(int(id), datetime.strptime(date, "%Y-%m-%d"), int(score_own), int(score_rival), rival,
                                 place_of_play)
    return redirect(url_for('/contentmaker/matches'))


@_require_authorized
@contentmaker_blueprints.route("/matches", methods=["DELETE"])
def delmatches():
    id = request.form['id']
    ContentmakerService.del_match(int(id))
    return redirect(url_for('/contentmaker/matches'))


@_require_authorized
@contentmaker_blueprints.route("/profile", methods=["GET"])
def profileget():
    contentmakerService = current_user.get_control_object()
    return render_template('profile.html', contentmaker=contentmakerService.get_own_contentmaker())


@_require_authorized
@contentmaker_blueprints.route("/profile", methods=["POST"])
def profilepush():
    newpass = request.form['newpass']
    contentmakerService = current_user.get_control_object()
    contentmakerService.change_password(newpass)
    return redirect(url_for('/contentmaker/profile'))
