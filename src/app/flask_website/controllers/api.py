"""
Модуль реализует API приложения.
"""
from flask import render_template, Blueprint, request, jsonify
from flask_website import app, db
from flask_website.service import ClientService

api_blueprints = Blueprint('api', __name__, url_prefix='/api/v1.0.0/')


@api_blueprints.route("/news", methods=["GET"])
def api_news():
    resplist = []
    for news in ClientService.get_all_news():
        resplist.append(news.serialization())
    return jsonify(resplist)


@api_blueprints.route("/matches", methods=["GET"])
def api_matches():
    resplist = []
    for matche in ClientService.get_all_matches():
        resplist.append(matche.serialization())
    return jsonify(resplist)
