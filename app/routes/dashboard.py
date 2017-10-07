from flask import Blueprint, render_template, abort, request, redirect, url_for, flash


view = Blueprint('dashboard', __name__, template_folder='templates')

@view.route('/')
def index():
    return render_template('index.html')

@view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('dashboard.index'))
    return render_template('login.html', error=error)
