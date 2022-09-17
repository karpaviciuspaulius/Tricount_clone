from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tricount.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Full Name', validators=[DataRequired(),
     Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),
     Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat Password',
     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Vhat username is taken. Please choose another one.')

    def validate_email(self, email):
        eml = User.query.filter_by(email=email.data).first()
        if eml:
            raise ValidationError('That email is taken. Please choose another one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
     Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login ')

class UpdateAccountForm(FlaskForm):
    username = StringField('Full Name', validators=[DataRequired(),
     Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(),
     Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Vhat username is taken. Please choose another one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            eml = User.query.filter_by(email=email.data).first()
            if eml:
                raise ValidationError('That email is taken. Please choose another one.')

class GroupForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')

class BillForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Add')