from flask import Flask, session
from routes.auth import auth_bp

app = Flask(__name__)
app.secret_key = "SecretKey"

app.register_blueprint(auth_bp)


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return "Welcome to your dashboard!"


