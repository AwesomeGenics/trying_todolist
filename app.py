from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_session import Session
from app.auth import auth
from app.tasks import task_bp



app = Flask(__name__)
app.secret_key='akjjdfdfjifjisjj'
app.register_blueprint(auth)
app.register_blueprint(task_bp)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.run(debug=True, host='0.0.0.0')
