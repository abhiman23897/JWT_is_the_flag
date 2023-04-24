from flask import Flask, redirect, render_template, request, url_for
import jwt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    username = 'user'
    password = 'user'
    if request.method == 'POST':
        if request.form['username'] == username and request.form['password'] == password:
            token = jwt.encode({'username': username, 'is_admin': False}, '1234', algorithm='HS256')
            return redirect(url_for('images', token=token))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/flag1')
def flag1():
    return "Flag Part 1: {insert flag part here}"

@app.route('/robots.txt')
def robots_txt():
    return "User-agent: *\nDisallow:\n\nFlag Part 2: {insert flag part here}"

@app.route('/robots')
def robots():
    return "Random text on robots"

@app.route('/stereogram')
def stereogram():
    return render_template('stereogram.html')

@app.route('/admin')
def admin():
    token = request.args.get('token')
    try:
        jwt.decode(token, '1234', algorithms=['HS256'])
    except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError):
        return render_template('unauthorized.html')
    return "Flag Part 4: {insert flag part here}"    

if __name__ == '__main__':
    app.run(host='localhost', port=5000)