import os
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '>\x8e\xaf}\x11`n\xd62\x8a\x98>a\x0b\xe1\x1d-V\x00\xa0^\xff[\xcb\xaa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)    # this is imported in models.py 

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)

import models
import views
#^ These are needed here to initialize Models only once (required by SQLALchemy)
