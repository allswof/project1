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
    headline="Welcome to the world of books!"
    return render_template("index.html", headline=headline)
    

@app.route("/login")
def login():
    headline="Log in"
    return render_template("login.html", headline=headline)

@app.route("/logoff")
def logoff():
    headline="Good bye!"
    return render_template("logoff.html", headline=headline)

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

    # if the username is available it adds it to the db
    if db.execute("SELECT * FROM users WHERE user_name = :name", {"name":name}).rowcount == 0:
        db.execute("INSERT INTO users (user_name, email, password) VALUES (:name, :email, :password)",
              {"name":name, "email":email, "password":password})
        db.commit()
        headline="Search"
        return render_template("search.html", headline=headline)
    else:
        headline="User name already taken"
        return render_template("index.html", headline=headline)

@app.route("/search")
def search():
    headline="Search"
    return render_template("search.html", headline=headline)

