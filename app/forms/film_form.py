import wtforms
from wtforms.validators import DataRequired, length
from flask_wtf import FlaskForm

class FilmForm(FlaskForm):
    title = wtforms.StringField(validators=[DataRequired(), length(max=200)])
    description = wtforms.TextAreaField()
    release_date = wtforms.DateField(validators=[DataRequired()])