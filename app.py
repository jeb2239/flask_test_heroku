
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
# from models import index_model

from flask_heroku import Heroku

# app = Flask(__name__)
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# heroku = Heroku(app)
# db = SQLAlchemy(app)

# jon = index_model.Index('904')

# @app.route('/')
# def index():
#     db.session.add(jon)
#     return 'Yo, its working!'





# if __name__ == "__main__":
#     app.run()
import os
import uuid
import sqlalchemy

import imhere

from flask_heroku import Heroku


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
imhere.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
heroku = Heroku(imhere.app)
db = SQLAlchemy(imhere.app)
imhere.app.secret_key = str(uuid.uuid4())

# imhere.app.config['db'] = db


imhere.app.run()
