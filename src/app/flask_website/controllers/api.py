"""
Модуль реализует API приложения.
"""
from flask import render_template, Blueprint, request, jsonify
from flask_website import app, db
from flask_website.service import ClientService

api_blueprints = Blueprint('api', __name__, url_prefix='/api/1.0.0')


@api_blueprints.route("/news", methods=["GET"])
def api_news():
    resplist = ClientService.get_all_news()
    return jsonify(resplist)


@api_blueprints.route("/matches", methods=["GET"])
def api_matches():
    resplist = ClientService.get_all_matches()
    return jsonify(resplist)
