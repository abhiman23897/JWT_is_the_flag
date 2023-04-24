from functools import wraps
from flask import Flask, jsonify, make_response, redirect, render_template, request, url_for
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_header
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '1234' # weak secret key for example purposes
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400
    if not username.isalnum() or not password.isalnum():
        return jsonify({'msg': 'Invalid username or password'}), 401
    if password != username[::-1]:
        return jsonify({'msg': 'Invalid username or password'}), 401
    user = {
        'username': username,
        'is_admin': False
    }
    access_token = create_access_token(identity=username, additional_headers=user)
    return jsonify({'access_token': access_token}), 200

@app.route('/api/items', methods=['GET'])
@jwt_required()
def items():
    items = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return items, 200

@app.route('/api/items/<item>', methods=['GET'])
@jwt_required()
def get_item(item):
    return item, 200

@app.route('/flag', methods=['GET'])
@jwt_required()
def flag():
    headers = get_jwt_header()
    if not headers['is_admin']:
        return jsonify({'msg': 'You do not have sufficient privileges to access this resource'}), 403
    return jsonify({'flag': 'CTF{example_flag}'}), 200

CORS(app)
if __name__ == '__main__':
    app.run(host='localhost', port=5000)