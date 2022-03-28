
from flask_bcrypt import Bcrypt #bcrypt is handled in the controllers (Models)
from flask import Flask,flash
import re

application = Flask(__name__)

#👇 We need this for session/flash
application.secret_key = "shhhhhhhhhhh!"