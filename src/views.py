from flask import render_template, request, redirect, session, flash, url_for,abort
from flask_login import LoginManager, login_required, login_user
from .main import app
from . import models
from . import forms

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return models.User()

@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/search')
@app.route('/results.html')
def search():
    site = request.args.get('site','')
    data = models.SearchResult.search(site)
    return render_template('results.html', results = data, search_input=site)

@app.route('/admin', methods=['POST', 'GET'])
@login_required
def admin_view():
    form = forms.SearchResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/')
    return render_template('admin.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = forms.LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)