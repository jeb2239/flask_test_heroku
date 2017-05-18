
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

from flask_heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Yo, its working!'



if __name__ == "__main__":
    app.run()
