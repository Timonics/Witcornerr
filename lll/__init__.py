from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'fd4003b2d237c1a54bda375e'
db = SQLAlchemy(app)

from lll import routes
