from flask import Flask, render_template, g, request, redirect, url_for
from flask.ext.assets import Bundle, Environment
from flask_debugtoolbar import DebugToolbarExtension

# Application configuration
app = Flask(__name__)
assets = Environment(app)

app.config.from_object('config')
app.config.from_object('instance.config')

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

from webint import views