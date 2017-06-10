from flask import render_template, request, redirect, session
from .main import app
from . import models
from . import forms

@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/search')
@app.route('/results.html')
def search():
    site = request.args.get('site','')
    data = models.SearchResult.search(site)
    datum_title = [datum.title for datum in data]
    for _ ,value in enumerate(datum_title):
        if not session.get(value):
            session[value] = 0
        session[value] += 1
    return render_template('results.html', results = data, search_input=site, session_counter=session)

@app.route('/admin', methods=['POST', 'GET'])
def admin_view():
    form = forms.SearchResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('/')
    return render_template('admin.html', form=form)