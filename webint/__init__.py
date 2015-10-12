from flask import Flask
from flask.ext.assets import Bundle, Environment
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from werkzeug.contrib.fixers import ProxyFix
# from flask_wtf.csrf import CsrfProtect
import coh

# XXX: we remove disfluency metrics. Check how to deal with them properly.
# for i, category in enumerate(coh.all_metrics.categories):
#     if isinstance(category, coh.Disfluencies):
#         del coh.all_metrics.categories[i]
#         break

# Application configuration
app = Flask(__name__, instance_relative_config=True)
app.wsgi_app = ProxyFix(app.wsgi_app)

# CsrfProtect(app)
assets = Environment(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

coh.config.from_object('config')

toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

# Bundles for joining and minifying CSS and JS files
bundles = {
    'css': Bundle('bower_components/bootstrap/dist/css/bootstrap.css',
                  'bower_components/CodeMirror/lib/codemirror.css',
                  'css/cmd.css',
                  filters='cssmin',
                  output='dist/index.min.css'),
    'js': Bundle('bower_components/jquery/dist/jquery.js',
                 'bower_components/bootstrap/dist/js/bootstrap.js',
                 'bower_components/bootbox/bootbox.js',
                 'bower_components/CodeMirror/lib/codemirror.js',
                 filters='rjsmin',
                 output='dist/cmd.min.js'),
}

assets.register(bundles)

from webint import views
from webint import models
from webint import forms
