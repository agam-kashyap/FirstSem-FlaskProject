from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Length,Email , EqualTo, ValidationError
from __main__ import db,User
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=5, max=20)])
    
    email = StringField('Email',validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    
    age = StringField('Age',validators=[DataRequired(),Length(min =1,max=3)])
    
    gender = StringField('Gender',validators=[DataRequired(),Length(min =4,max=6)])
    
    phone = StringField('Phone',validators=[DataRequired(),Length(min=10,max=10)])
    
    address = StringField('Address',validators=[DataRequired(),Length(min =1,max=200)])
    
    submit = SubmitField('Sign Up')
    
    def validate_phone(form, phone):
        if len(phone.data) > 10:
            raise ValidationError('Invalid phone number.')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        
        if user:
            raise ValidationError('This username already exists.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        
        if user:
            raise ValidationError('This email has already been taken.')


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
