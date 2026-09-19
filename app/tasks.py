from flask import render_template, redirect, url_for, Blueprint, blueprints, request, flash, session
from app.db import conn, csr
from flask_session import Session

task_bp = Blueprint('task_bp', __name__)


@task_bp.route('/add', methods=['GET','POST'])
def add_task():
    if not session.get('name'):
        flash('Login to access that page')
        return redirect('/login')
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task != '':
            a = f'INSERT INTO owner_task (owner, task_name) VALUES (?,?)'
            csr.execute(a, (session['name'], new_task,))
            conn.commit()
        else:
            flash('Task cannot be empty')
            return redirect('/add')

    return render_template('newtask.html')


@task_bp.route('/home', methods=['GET','POST'])
def task_list():
    if request.method == 'POST':
        csr.execute('DELETE FROM owner_task')
        conn.commit()

    if not session.get('name'):
        flash('Login to access that page')
        return redirect('/login')
    else:
        result = csr.execute('SELECT * FROM owner_task WHERE owner = ?',
                             (session['name'],))
        return render_template('listview.html', tasksaslist = result)
    

# So inputing num in decorator makes it available to use for python ops
@task_bp.route('/delete/<int:num>', methods=['GET','POST'])
def delete(num):
    a = f'DELETE FROM owner_task WHERE id = ?'
    csr.execute(a, (num,))
    conn.commit()
    return redirect('/home')
