from flask import Flask, render_template, request 
app = Flask(__name__) 
@app.route('/') 
def index(): 
	return render_template('front.html')
@app.route('/login')
def login():
	return render_template('login.html')
@app.errorhandler(404) 
def page_not_found(e): 
	return render_template('error.html'), 404
if __name__ == '__main':
	app.run(debug = True)
