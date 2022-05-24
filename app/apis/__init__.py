from sanic import Blueprint

from app.apis.blueprint import links_blueprint

api = Blueprint.group([links_blueprint])