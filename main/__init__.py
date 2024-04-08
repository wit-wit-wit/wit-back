from flask import Flask
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://gun7728:FuvEduCUdIrwcdlt@wit.1hikp2t.mongodb.net/?retryWrites=true&w=majority&appName=wit'
now = str(datetime.now())
db = PyMongo(app).cx['wit']

from . import comment
from . import user

app.register_blueprint(comment.blueprint)
app.register_blueprint(user.blueprint)
