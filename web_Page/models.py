from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, PickleType, String, Enum, DATE, URL
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
import logging as lg
import enum

from .views import app

# Create database connection object
db = SQLAlchemy(app)

date = datetime.today()

class Gender(enum.Enum):
    Biologie = 0
    Numerique = 1
    Societé = 2


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    date = Column(DATE, nullable=False)
    autor_id =Column(MutableList.as_mutable(PickleType), default=list[int])
    file = Column(String(200), nullable=False)
    img = Column(String(200), nullable=False)


    def __init__(self, id, title, gender, date, autor_id, file, img):
        self.id = id
        self.title = title
        self.gender = gender
        self.date = date
        self.autor_id = autor_id  
        self.file = file
        self.img = img

class Autor(db.Model):
    id = Column(Integer, primary_key=True)
    nom = Column(String(200), nullable=False)
    prenom = Column(String(200), nullable=False)
    
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Article(1, "article 1", Gender.Biologie, date, [1,5], "article1.pdf", "blog-1.jpg"))
    db.session.add(Autor(1,"Desbles", "Loann"))
    db.session.add(Autor(5,"Le garrec", "Aël"))
    db.session.commit()
    lg.warning("Database initialized!")

    



