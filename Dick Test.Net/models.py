from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dick(db.Model):
    __tablename__ = "Dicks"
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable=False)
    IP = db.Column(db.String, nullable=False)
    cid = db.Column(db.String, db.ForeignKey("countries.id"), nullable=False)

class Country(db.Model):
    __tablename__ = "countries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
