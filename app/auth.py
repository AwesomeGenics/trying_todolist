from flask import render_template, redirect, url_for, Blueprint, blueprints, request, flash, session
from app.db import conn, csr
from flask_session import Session

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        email = request.form.get('email')
        a = csr.execute('''SELECT * FROM task_list WHERE name = ?''', (name,))
        b = a.fetchone()

        if b:
            flash('Account already exists')
            return redirect('/register')
        else:
            if name and email and pwd:
                csr.execute('''INSERT INTO task_list(
                name, password, email) VALUES (?,?,?)''',(name, pwd, email,))
                conn.commit()
                return redirect('/login')
            else:
                flash('No Field can be left empty!')
                return redirect('/register')
    return render_template('register.html')



@auth.route('/', methods=['GET','POST'])
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        
        if name and pwd:
            only_name = csr.execute('SELECT * FROM task_list WHERE name = ?',
                            (name,))
            b = only_name.fetchone()
            if not b:
                flash('No account exists with that name. Please register')
                return redirect('/login')
            elif b['password'] == pwd:
                session['name'] = name
                return redirect('/home')
            elif b['password'] != pwd:
                flash('Wrong credentials entered')
                return redirect('/login')
            
        else:
            flash('Credentials cannot be empty.')
            return redirect('/login')
    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
