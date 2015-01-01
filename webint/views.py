from flask import render_template, request, redirect, url_for
from webint import app

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
	return 'You tried to register: ' + str(request.form)


@app.route('/login', methods=['POST'])
def login():
	return redirect(url_for('analyze'))


@app.route('/analyze')
def analyze():
	return render_template('analyze.html')


@app.route('/submit', methods=['POST'])
def submit():
	return 'You tried to submit a text: ' + str(request.form)