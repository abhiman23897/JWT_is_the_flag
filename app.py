from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_header
)

app = Flask(__name__)
jwt = JWTManager(app)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400
    if not username.isalnum() or not password.isalnum():
        return jsonify({'msg': 'Invalid username or password'}), 401
    if not len(username) == 10:
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
    items = ['Apple', 'Banana', 'Car', 'Dog', 'Elephant', 'Flag', 'Grapes', 'House', 'Ice cream', 'Jacket', 'Kangaroo', 'Lion', 'Mango', 'Nest', 'Orange', 'Pencil', 'Queen', 'Rainbow', 'Sun', 'Tree', 'Umbrella', 'Van', 'Watch', 'Xylophone', 'Yak', 'Zebra']
    return items, 200

@app.route('/api/items/<item>', methods=['GET'])
@jwt_required()
def get_item(item):
    headers = get_jwt_header()
    if item == "Flag" and not headers['is_admin']:
            return jsonify({'msg': 'You do not have sufficient privileges to access this resource'}), 403
    
    return send_file(f'static/{item.lower()}.png', mimetype='image/png')


#TODO: Move this to a config file
app.config['JWT_SECRET_KEY'] = 'super_secret_key@123'

if __name__ == '__main__':
    print(app.config)
    app.run(host='localhost', port=5000)