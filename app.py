import imhere
import os
from sqlalchemy import *
import uuid
from flask_heroku import *
def get_app():

    imhere.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    # heroku = Heroku(imhere.app)
    db = create_engine((imhere.app.config['SQLALCHEMY_DATABASE_URI']),
                       pool_size=1)
    imhere.app.config['db'] = db

    imhere.app.secret_key = str(uuid.uuid4())
    return imhere.app