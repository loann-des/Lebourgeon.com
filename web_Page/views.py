from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import logging as lg
from config import config as c
import os

app = Flask(__name__)
app.config.from_object("config.config")

mail = Mail(app)


@app.route("/")
@app.route("/index/")
def index():
    """Renders the main index page of the website.

    Handles requests to the root and '/index/' URLs and returns the index HTML template.

    Returns:
        A rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/blog")
@app.route("/blog/")
def blog():
    """Renders the blog page of the website.

    Handles requests to the '/blog' and '/blog/' URLs and returns the blog HTML template.

    Returns:
        A rendered HTML template for the blog page.
    """
    return render_template("blog.html")


@app.route("/blog/blog-details")
@app.route("/blog/blog-details/")
def blog_details():
    return render_template("blog-details.html")


@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        msg = Message(subject, sender=email, recipients=[app.config["MAIL_USERNAME"]])
        msg.body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)
        return "OK"
    except Exception as e:
        lg.warning(f"Erreur lors de l'envoi de l'email : {e}")

        return str(e), 500


@app.route("/upload-page", methods=["GET"])
def upload():
    return render_template("upload.html")


@app.route("/upload_article", methods=["POST"])
def upload_article():
    from .models import upload_article as upd
    from .models import Gender

    try:
        title = request.form["title"]
        gender = Gender[request.form["gender"]]  # convertit string en Enum
        date = datetime.now().date()
        autor_id_raw = request.form.get("autor_id", "")
        autor_ids = [
            int(id.strip()) for id in autor_id_raw.split(",") if id.strip().isdigit()
        ]
        pdf = request.files["file"]
        img = request.files["img"]

        if not (pdf and img):
            return "Fichier ou image manquant", 400

        lg.info("Création d’un nouvel article...")
        upd(title=title, gender=gender, date=date, autor_ids=autor_ids, pdf=pdf, img=img)
        return redirect(url_for("blog"))

    except Exception as e:
        lg.error(f"Erreur pendant l’upload : {e}")
        return f"Erreur : {str(e)}", 500
