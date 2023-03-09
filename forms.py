from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# TODO: add proper validators & fields for variables instead of all StringField
class BookingForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    duration = StringField("# of Night", validators=[DataRequired()])
    submit = SubmitField("Book Me!")


class MonthForm(FlaskForm):
    month = StringField("Month", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    submit = SubmitField("Change Month")
