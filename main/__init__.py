from flask import Flask
from pymongo import MongoClient
from datetime import datetime
import certifi

ca = certifi.where()

app = Flask(__name__)
client = MongoClient('mongodb+srv://gun7728:FuvEduCUdIrwcdlt@wit.1hikp2t.mongodb.net/?retryWrites=true&w=majority&appName=wit',tlsCAFile=ca)
now = str(datetime.now())
db = client.wit

from . import comment
from . import user

app.register_blueprint(comment.blueprint)
app.register_blueprint(user.blueprint)
