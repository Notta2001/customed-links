from sanic import Blueprint
from sanic.response import json
from app.databases.mongodb import MongoDB

links_blueprint = Blueprint('links_blueprint', url_prefix='/links')

_db = MongoDB()


@links_blueprint.route('/create-customed-link', methods={'POST'})
async def create_customed_link(request):
    nonce = _db.find_nonce_link(request.json['url'])
    _db.create_customed_link(request.json['url'], nonce)
    return json({
        'message': 'success',
    })


@links_blueprint.route('/get-all-customed-link', methods={'GET'})
async def get_all_customed_link(request):
    data = _db.get_all_customed_link(request.args.get('url'))
    nonce = _db.find_nonce_link(request.args.get('url'))
    return json({
        'nonce': nonce,
        'links': list(data)
    })


@links_blueprint.route('/get-origin-url', methods={'GET'})
async def get_origin_url(request):
    data = _db.get_origin_url(request.args.get('link'))
    return json(data)


@links_blueprint.route('/test', methods={'GET'})
async def test(request):
    _db.views_count()
    return json({
        'message': 'success',
    })

@links_blueprint.route('/get-view-logs', methods={'GET'})
async def get_view_logs(request):
    data = _db.get_views_log(request.args.get('url'))
    return json(data)

