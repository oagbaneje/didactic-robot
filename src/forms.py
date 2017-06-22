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

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])

    def validate(self):
        result = super().validate()
        email = self.data['email']
        password = self.data['password']
        if email and password:
            if email == 'learner@example.com' and password== 'password':
                return True
            self.email.errors.append('The email/password combination is wrong')
        return False