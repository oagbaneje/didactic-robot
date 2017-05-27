import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'database.db'))
app.config["SECRET_KEY"] = "hello"


db = SQLAlchemy()

class SearchResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String)
    summary = db.Column(db.String())

    def __repr__(self):
        return "<SearchResult {}>".format(self.title)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        new_data = SearchResult(**kwargs)
        new_data.save()

    @classmethod
    def populate_with_data(cls):
        data = {
        "title": "Jinja",
        "url": "/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQFgghMAA&amp;url=http%3A%2F%2Fjinja.pocoo.org%2F&amp;usg=AFQjCNFKiObWsstA_tSpH_tNsUK_VKY4EA&amp;sig2=eFKaff1ZCmdBpLeG3og3Uw",
        "summary": """<div class="s">
                    <div>
                        <div class="f kv _SWb" style="white-space:nowrap"><cite class="_Rm">jinja.pocoo.org/</cite>
                            <div class="action-menu ab_ctl"><a class="_Fmb ab_button" href="#" id="am-b0" aria-label="Result details" aria-expanded="false"
                                    aria-haspopup="true" role="button" jsaction="m.tdd;keydown:m.hbke;keypress:m.mskpe" data-ved="0ahUKEwi6zevKr_7TAhUJiSwKHblZAeUQ7B0IIjAA"><span class="mn-dwn-arw"></span></a>
                        </div>
                        </div><span class="st"><em>Jinja</em> is Beautiful. {% extends "layout.html" %} {% block body %} &lt;ul&gt; {% for user in users %} &lt;li&gt;&lt;a href="{{ user.url }}"&gt;{{ user.username }}&lt;/a&gt;&lt;/li&gt; {% endfor&nbsp;...</span></div>
                </div>"""
        }
        inst = cls(**data)
        inst.save()

db.init_app(app)

class SearchResultForm(FlaskForm):
    title = StringField("The title of the page", validators=[DataRequired()])
    url = StringField("The url of the page", validators=[DataRequired()])
    summary = StringField("Search Summary", widget=TextArea(), validators=[DataRequired()])

    def save(self):
        SearchResult.create(title=self.data['title'], url=self.data['url'], summary=self.data['summary'])

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/search')
@app.route('/results.html')
def search():
    site = request.args.get('site')
    data = SearchResult.query.all()
    return render_template('results.html', results = data, search_input=site)

@app.route('/admin', methods=['POST', 'GET'])
def admin_view():
    form = SearchResultForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            form.save()
            return redirect('search')
    return render_template('admin.html', form=form)