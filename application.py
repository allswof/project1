import os

from flask import Flask, render_template, session, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    headline="Register"
    return render_template("index.html", headline=headline)

@app.route("/login")
def login():
    headline="Log in"
    return render_template("login.html", headline=headline)

@app.route("/logoff")
def logoff():
    headline="Good bye!"
    return render_template("logoff.html", headline=headline)

@app.route("/register", methods="POST")
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = reques.form.get(password)


