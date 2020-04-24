import os
from flask import render_template, Blueprint, request, url_for, redirect

from flask_website import app, db


contentmaker_blueprints = Blueprint(name='contentmaker', import_name=__name__, template_folder=os.path.join(app.config['TEMPLATE_FOLDER'], 'contentmaker'), url_prefix='/contentmaker')


@contentmaker_blueprints.route("/", methods=["GET"])
def root():
    return render_template("main.html")


@contentmaker_blueprints.route("/news", methods=["GET"])
def news():
    st = request.args['st']
    return render_template("news.html")


@contentmaker_blueprints.route("/news/new", methods=["GET"])
def newnews():
    newid = 0
    return redirect(url_for('/contentmaker/news/'+newid+'/edit'))


@contentmaker_blueprints.route("/news/<id>/edit", methods=["GET"])
def editnewsget():
    return render_template("editnews.html")


@contentmaker_blueprints.route("/news/<id>/edit", methods=["POST"])
def editnewspush():
    header = request.form['header']
    body = request.form['body']
    date = request.form['date']
    return redirect(url_for('/contentmaker/news'))


@contentmaker_blueprints.route("/news/<id>", methods=["DELETE"])
def delnews(id):
    return redirect(url_for('/contentmaker/news'))


@contentmaker_blueprints.route("/matches", methods=["GET"])
def matches():
    st = request.args['st']
    return render_template("matches.html")


@contentmaker_blueprints.route("/matches/new", methods=["GET"])
def newmatches():
    newid = 0
    return redirect(url_for('/contentmaker/matches/'+newid+'/edit'))


@contentmaker_blueprints.route("/matches/<id>/edit", methods=["GET"])
def editmatchesget():
    return render_template("editmatches.html")


@contentmaker_blueprints.route("/matches/<id>/edit", methods=["POST"])
def editmatchespush():
    date = request.form['date']
    score_own = request.form['score_own']
    score_rival = request.form['score_rival']
    rival = request.form['rival']
    place_of_play = request.form['place_of_play']
    return redirect(url_for('/contentmaker/matches'))


@contentmaker_blueprints.route("/matches/<id>", methods=["DELETE"])
def delmatches(id):
    return redirect(url_for('/contentmaker/matches'))


@contentmaker_blueprints.route("/profile", methods=["GET"])
def profileget(id):
    return render_template('profile.html')


@contentmaker_blueprints.route("/profile", methods=["POST"])
def profilepush():
    newpass = request.form['newpass']
    return redirect(url_for('/contentmaker/profile'))

