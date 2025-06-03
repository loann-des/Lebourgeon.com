from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import FileStorage
from sqlalchemy import Column, Integer, PickleType, String, Enum, DATE, URL, LargeBinary
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
import logging as lg
import enum

from .views import app

# Create database connection object
db = SQLAlchemy(app)

date = datetime.now()


class Gender(enum.Enum):
    Fiction = "Fiction"
    NonFiction = "NonFiction"
    Poetry = "Poetry"
    Other = "Other"


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    date = Column(DATE, nullable=False)
    autor_id = Column(MutableList.as_mutable(PickleType), default=list[int])
    file = Column(String(20))
    img = Column(String(20))

    def __init__(self, title, gender, date, autor_id, file, img):
        self.title = title
        self.gender = gender
        self.date = date
        self.autor_id = autor_id
        self.file = file
        self.img = img


class Autor(db.Model):
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


class Upload(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    data = Column(LargeBinary)

    def __init__(self, name, data):
        self.name = name
        self.data = data


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Autor("Desbles", "Loann"))
    db.session.add(Autor("Le garrec", "Aël"))
    db.session.commit()
    lg.warning("Database initialized!")


def upload_article(
    title: str, gender: Gender, date: DATE, autor_ids: list[int], pdf: FileStorage, img: FileStorage
):
    from .fonction import rename

    new_article = Article(
        title=title, gender=gender, date=date, autor_id=autor_ids, file="", img=""
    )
    db.session.add(new_article)
    db.session.flush()

    article_id = new_article.id
    new_article.file, new_article.img = rename(pdf, img, article_id)

    db.session.commit()

