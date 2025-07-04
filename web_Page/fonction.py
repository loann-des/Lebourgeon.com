import os
from .views import app
import logging as lg
from config import config as c
import enum
from .models import Article, Autor
from werkzeug.datastructures import FileStorage


class Val(enum.Enum):
    E_MAIL = c.E_MAIL
    E_MAIL_LINK = c.E_MAIL_LINK
    INSTA = c.INSTA
    TEL = c.TEL
    LINKEDIN = c.LINKEDIN
    ADHESION = c.ADHESION
    DONS = c.DONS


basedir = os.path.abspath(os.path.dirname(__file__))
URI = os.path.join(basedir, "txt")


def word_at_index(index: int, txt: str) -> str:
    return txt.split(" ")[index + 1]


def mdw(txt: str) -> str:
    return word_at_index(-1, txt)


def txt_from_index(index: int, txt: str) -> str:
    index += 1
    return "".join([" " + word for word in txt.split(" ")[index:]])


def txtOf(txt: str) -> str:
    return txt_from_index(0, txt)


def text_from(file_name: str, title: bool = False):
    file_name = file_name + ".txt"
    path = os.path.join(URI, file_name)
    try:
        with open(path, "r", encoding="UTF-8") as f:
            if title:
                return f.readline().replace("\n", "")
            else:
                return f.readlines()[1].replace("\n", "")
    except Exception as ex:
        lg.warning(ex)


def html_from(file_name: str, section: int):
    file_name += ".txt"
    path = os.path.join(URI, file_name)
    try:
        with open(path, "r", encoding="UTF-8") as f:
            start = 0
            lignes = f.readlines()
            res = []
            for l in lignes:
                if l[:3] == "§§§":
                    start += 1
                elif start == section:
                    res.append(l)
                if start > section:
                    return res
        return res
    except Exception as ex:
        lg.warning(ex)


def get_ref(val):
    match val:
        case "E_MAIL":
            return Val.E_MAIL.value
        case "E_MAIL_LINK":
            return Val.E_MAIL_LINK.value
        case "INSTA":
            return Val.INSTA.value
        case "TEL":
            return Val.TEL.value
        case "LINKEDIN":
            return Val.LINKEDIN.value
        case "ADHESION":
            return Val.ADHESION.value
        case "DONS":
            return Val.DONS.value


def get_article(article_id: int) -> Article:
    return Article.query.get_or_404(article_id)


def get_AllArticle() -> list[Article]:
    for x in Article.query.all():
        print(
            f"{x.id}, {x.title}, {x.gender.name}, {x.date}, {x.autor_id} , {x.file}, {x.img}"
        )
    return Article.query.all()


def get_Autor(id):
    for x in Autor.query.filter(Autor.id.in_(id)).all():
        print(f"{x.id}, {x.nom}, {x.prenom}")  # TODO remove print
    return Autor.query.filter(Autor.id.in_(id)).all()


def str_(x: int):
    return str(x)


def rename(pdf: FileStorage, img: FileStorage, article_id: int) -> tuple[str, str]:
    # Extensions
    pdf_ext = os.path.splitext(pdf.filename)[1] or ".pdf"
    img_ext = os.path.splitext(img.filename)[1] or ".jpg"

    # Noms automatiques
    pdf_filename = f"blog-{article_id}{pdf_ext}"
    img_filename = f"blog-{article_id}{img_ext}"

    # Chemins complets
    pdf_path = os.path.join("web_Page/static/pdf", pdf_filename)
    img_path = os.path.join("web_Page/static/images/blog", img_filename)

    # Sauvegarde
    pdf.save(pdf_path)
    img.save(img_path)

    # Retourner les chemins relatifs depuis "static/"
    return f"pdf/{pdf_filename}", f"images/blog/{img_filename}"


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
