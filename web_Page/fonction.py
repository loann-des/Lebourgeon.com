import os
from .views import app
import logging as lg
import config as c
import enum
from .models import Article, Autor



class Val(enum.Enum):
    E_MAIL = c.E_MAIL
    E_MAIL_LINK = c.E_MAIL_LINK
    INSTA = c.INSTA
    TEL = c.TEL
    LINKEDIN = c.LINKEDIN
    ADHESION = c.ADHESION
    DONS = c.DONS


basedir = os.path.abspath(os.path.dirname(__file__))
URI = os.path.join(basedir, 'txt')

def word_at_index(index : int, txt : str)->str:
    return txt.split(' ')[index+1]

def mdw(txt : str)->str :
    return word_at_index(-1, txt)


def txt_from_index(index : int, txt : str)->str :
    index += 1
    return ''.join(
        [' ' + word for word in txt.split(' ')[index:]]
        )
    
def txtOf(txt : str)->str :
    return txt_from_index(0, txt)

def text_from(file_name: str, title: bool = False):
    file_name = file_name + '.txt'
    path = os.path.join(URI, file_name)
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            if (title):
                return f.readline().replace("\n", "")
            else:
                return f.readlines()[1].replace("\n", "")
    except Exception as ex:
        lg.warning(ex)
    

def html_from(file_name: str, section: int):
    file_name = file_name + '.txt'
    path = os.path.join(URI, file_name)
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            start = 0
            lignes = f.readlines()
            res = []
            for l in lignes:
                if (l[0:3] == '§§§'):
                    start += 1
                elif (start == section):
                    res.append(l)
                if (start > section):
                    return res
        return res
    except Exception as ex:
        lg.warning(ex)


def get_ref(val):
    match val:
        case 'E_MAIL':
            return Val.E_MAIL.value
        case 'E_MAIL_LINK':
            return Val.E_MAIL_LINK.value
        case 'INSTA':
            return Val.INSTA.value
        case 'TEL':
            return Val.TEL.value
        case 'LINKEDIN':
            return Val.LINKEDIN.value
        case 'ADHESION':
            return Val.ADHESION.value
        case 'DONS':
            return Val.DONS.value


def get_AllArticle() -> list[Article]:
    for x in Article.query.all():
        print(f"{x.id}, {x.title}, {x.gender.name}, {x.date}, {x.autor_id} , {x.file}, {x.img}")
    return Article.query.all()

def get_Autor(id) :
    for x in Autor.query.filter(Autor.id.in_(id) ).all():
        print(f"{x.id}, {x.nom}, {x.prenom}")
    return Autor.query.filter(Autor.id.in_(id) ).all()

def str_(x : int) :
    return str(x)



app.jinja_env.globals.update(mdw=mdw)
app.jinja_env.globals.update(txtOf=txtOf)
app.jinja_env.globals.update(word_at_index=word_at_index)
app.jinja_env.globals.update(txt_from_index=txt_from_index)
app.jinja_env.globals.update(text_from=text_from)
app.jinja_env.globals.update(html_from=html_from)
app.jinja_env.globals.update(get_ref=get_ref)
app.jinja_env.globals.update(get_AllArticle=get_AllArticle)
app.jinja_env.globals.update(get_Autor=get_Autor)
app.jinja_env.globals.update(str_=str)
