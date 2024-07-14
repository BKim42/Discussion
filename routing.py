from flask import Flask, render_template
app = Flask(__name__) 
@app.route('/') 
def index(): 
	render_template('base.html')
if __name__ == '__main':
	app.run()
