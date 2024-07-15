from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField, validators 
from wtforms.validators import DataRequired
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'placeholder'
class SignUpForms(FlaskForm):
	firstname = StringField("First Name: ") 
	lastname = StringField("Last Name: ")
	username = StringField("Username: ")
	password = StringField("Password: ")
	grade = RadioField("Grade Level: ", choices=[("ninth", "9th"), ("tenth", "10th"), ("eleventh, 11th"), ("twelveth, 12th")])
	submit = SubmitField("Submit")
@app.route('/') 
def index(): 
	return render_template('front.html')
@app.route('/', methods = ['GET', 'POST'])
def login():
	firstname = False 
	lastname = False
	username = False 
	password = False 
	grade = False
	form = SignUpForms()
	if form.validate_on_submit():
		firstname = form.firstname.data	
		lastname = form.lastname.data
		username = form.username.data
		password = form.password.data
		grade = form.grade.data 
	return render_template('signin.html', firstname = firstname, lastname = lastname, username = username, password = password, grade = grade)
@app.errorhandler(404) 
def page_not_found(e): 
	return render_template('error.html'), 404
if __name__ == '__main':
	app.run(debug = True)
