
# Import flask and template operators
from datetime import date

from flask import Flask, render_template

# Import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
today = date.today()
t = today.strftime("%Y")  # Configurations
try:
    app.config.from_object('config')
except:
    print("Debe renombrar el archivo config.orig a config.py")
    app.config.from_object('config')

from app.modWorld.controller import mod_world

app.register_blueprint(mod_world)