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
from flask_website.controllers.root import get_first_future_match, get_micro_mews

contentmaker_blueprints = Blueprint(name='contentmaker', import_name=__name__, url_prefix='/contentmaker')


def _require_authorized():
    if not current_user.is_authenticated:
        return render_template("_401.html"), 401
    elif current_user.get_user_role() != UserRole.contentmaker:
        return render_template("_401.html"), 401
    else:
        return None


@contentmaker_blueprints.route("/", methods=["GET"])
def root():
    if _require_authorized() is not None:
        return _require_authorized()
    return render_template("contentmaker/main.html")


@contentmaker_blueprints.route("/news", methods=["GET"])
def news():
    if _require_authorized() is not None:
        return _require_authorized()
    return render_template("contentmaker/news.html", micronews=get_micro_mews(0), future_match=get_first_future_match())


@contentmaker_blueprints.route("/news/new", methods=["GET"])
def getnewnewsform():
    if _require_authorized() is not None:
        return _require_authorized()
    return render_template("contentmaker/createthenews.html")


@contentmaker_blueprints.route("/news/new", methods=["POST"])
def createnewspush():
    if _require_authorized() is not None:
        return _require_authorized()
    header = request.form['header']
    body = request.form['body']
    date = request.form['date']
    time = request.form['time']
    ContentmakerService.add_new_news(header, body, datetime.strptime(date+'|'+ time, '%Y-%m-%d|%H:%M'))
    return redirect('/contentmaker/news')


@contentmaker_blueprints.route("/news", methods=["POST"])
def delnews():
    if _require_authorized() is not None:
        return _require_authorized()
    if request.form['action'] == 'delete':
        id = request.form['id']
        ContentmakerService.del_news(int(id))
        return redirect('/contentmaker/news')
    return redirect('/contentmaker/news')


@contentmaker_blueprints.route("/matches", methods=["GET"])
def matches():
    if _require_authorized() is not None:
        return _require_authorized()
    response_list_matches = ContentmakerService.get_all_matches()
    return render_template("contentmaker/matches.html", matchs=response_list_matches)


@contentmaker_blueprints.route("/matches/new", methods=["GET"])
def getnewmatchesform():
    if _require_authorized() is not None:
        return _require_authorized()
    return render_template("contentmaker/createthematche.html")


@contentmaker_blueprints.route("/matches/new", methods=["POST"])
def newmatchespush():
    if _require_authorized() is not None:
        return _require_authorized()
    date = request.form['date']
    time = request.form['time']
    score_own = request.form['score_own']
    score_rival = request.form['score_rival']
    rival = request.form['rival']
    place_of_play = request.form['place_of_play']
    ContentmakerService.add_new_match(datetime.strptime(date+'|'+time, '%Y-%m-%d|%H:%M'), int(score_own), int(score_rival), rival,
                                      place_of_play)
    return redirect('/contentmaker/matches')


@contentmaker_blueprints.route("/matches/change", methods=["GET"])
def geteditmatchesform():
    if _require_authorized() is not None:
        return _require_authorized()
    id = request.args.get('id')
    matche = ContentmakerService.get_thematch(int(id))
    return render_template("contentmaker/editthematche.html", matche=matche)


@contentmaker_blueprints.route("/matches/change", methods=["POST"])
def editmatchespush():
    if _require_authorized() is not None:
        return _require_authorized()
    id = request.form['id']
    date = request.form['date']
    time = request.form['time']
    score_own = request.form['score_own']
    score_rival = request.form['score_rival']
    rival = request.form['rival']
    place_of_play = request.form['place_of_play']
    ContentmakerService.ch_match(int(id), datetime.strptime(date+'|'+time, '%Y-%m-%d|%H:%M'), int(score_own),
                                 int(score_rival),
                                 rival,
                                 place_of_play)
    return redirect('/contentmaker/matches')


@contentmaker_blueprints.route("/matches", methods=["POST"])
def delmatches():
    if _require_authorized() is not None:
        return _require_authorized()
    if request.form['action'] == 'delete':
        id = request.form['id']
        ContentmakerService.del_match(int(id))
        return redirect('/contentmaker/matches')
    return redirect('/contentmaker/matches')


@contentmaker_blueprints.route("/profile", methods=["GET"])
def profileget():
    if _require_authorized() is not None:
        return _require_authorized()
    contentmakerService = current_user.get_control_object()
    return render_template('contentmaker/profile.html', contentmaker=contentmakerService.get_own_contentmaker())


@contentmaker_blueprints.route("/profile", methods=["POST"])
def profilepush():
    if _require_authorized() is not None:
        return _require_authorized()
    newpass = request.form['newpass']
    contentmakerService = current_user.get_control_object()
    contentmakerService.change_password(newpass)
    return redirect('/contentmaker/profile')
