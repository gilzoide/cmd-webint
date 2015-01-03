from flask import Flask
from flask.ext.assets import Bundle, Environment
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
import coh

# Application configuration
app = Flask(__name__, instance_relative_config=True)
assets = Environment(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)

coh.config.from_object('config')

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
from webint import models
from webint import forms
