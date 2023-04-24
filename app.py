from functools import wraps
from flask import Flask, jsonify, redirect, render_template, request, url_for
import jwt

app = Flask(__name__)

# Custom decorator to check JWT token for authentication
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        # Check for Authorization header
        if 'Authorization' in request.headers:
            # Get token from header
            auth_header = request.headers['Authorization']
            token_parts = auth_header.split(' ')
            if len(token_parts) == 2:
                token_type = token_parts[0]
                token = token_parts[1]

        if not token:
            return jsonify({'message': 'Authorization token is missing.'}), 401

        try:
            # Verify token with secret key
            data = jwt.decode(token, 1234, algorithms=['HS256'])
            current_user = {'username': data['username'], 'is_admin': data['is_admin']}
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token.'}), 401

        return func(current_user, *args, **kwargs)

    return decorated

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password.isalnum() and password[::-1] == username:
            jwt_payload = {
                'username': username,
                'is_admin': False
            }
            jwt_secret = '1234'
            token = jwt.encode(
                payload=jwt_payload,
                key=jwt_secret,
                algorithm='HS256')
            return redirect(url_for('dashboard'), 200, {"Authorization": "Bearer " + token})
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
@token_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin')
@token_required
def admin(current_user):
    if current_user['is_admin']:
        return render_template('flag.html')
    else:
        return render_template('unauthorized.html')
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)