from flask import Flask, render_template, g, request, redirect, url_for
from flask.ext.assets import Bundle, Environment
from flask_debugtoolbar import DebugToolbarExtension

# Application configuration
app = Flask(__name__)
assets = Environment(app)

app.debug=True

app.config['SECRET_KEY'] = 'development key'

toolbar = DebugToolbarExtension(app)

# Bundles for joining and minifying CSS and JS files
bundles = {
	'css': Bundle('bower_components/bootstrap/dist/css/bootstrap.css',
		 	      'css/cmd.css', 
				   filters='cssmin',
				   output='dist/index.min.css'),
	'js': Bundle('bower_components/jquery/dist/jquery.js',
				 'bower_components/bootstrap/dist/js/bootstrap.js',
				 filters='rjsmin',
				 output='dist/cmd.min.js'),
}

assets.register(bundles)

# Functions to handle URLs

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


if __name__ == '__main__':
	app.run()