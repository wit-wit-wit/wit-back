from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = str(datetime.now())

from . import comment
from . import user

app.register_blueprint(comment.blueprint)
app.register_blueprint(user.blueprint)
