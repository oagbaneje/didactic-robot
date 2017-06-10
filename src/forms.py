from flask_wtf import FlaskForm
from .models import SearchResult
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class SearchResultForm(FlaskForm):
    title = StringField("The title of the page", validators=[DataRequired()])
    url = StringField("The url of the page", validators=[DataRequired()])
    summary = StringField("Search Summary", widget=TextArea(), validators=[DataRequired()])

    def save(self):
        SearchResult.create(title=self.data['title'], url=self.data['url'], summary=self.data['summary'])