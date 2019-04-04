import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rcyzrftzwolqol:887eb42f233f9f28302d39c6e4d9f5c2d2442ac10fde169b250752adcfdb7ae6@ec2-184-73-153-64.compute-1.amazonaws.com:5432/dceap280ufaj0k'
db = SQLAlchemy(app)

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

def main():
    f = open("books.cvs")
    reader = csv.reader(f)

    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES(:isbn, :title, :author, :year)",
        {"isbn":isbn, "title":title, "author":author, "year":year})
        print(f"Added {title} to database.")

    db.commit()
