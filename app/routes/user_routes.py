# app/routes/user_routes.py
from flask import jsonify, request, abort
from app import app, cache
from app.services.user_service import get_user, create_user, get_all_users

@cache.cached(timeout=300, key_prefix='user_{user_id}')
@app.route('/user/<user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user(user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app.route('/user', methods=['POST'])
def create_user_route():
    data = request.get_json()
    user = create_user(data)
    return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    users_data = get_all_users(page=page, per_page=per_page)

    return jsonify(users_data)
