from flask import Flask ,render_template, request
from flask_mail import Mail, Message
import logging as lg
from config import config as c

app = Flask(__name__)


# app.config.from_object('config')
# Config options - Make sure you created a 'config.py' file.
app.config.from_object("config.config")


# To get one variable, tape app.config['MY_VARIABLE']
app.config["SQLALCHEMY_DATABASE_URI"] = c.SQLALCHEMY_DATABASE_URI

mail = Mail(app)

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/blog")
@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/blog/blog-details")
@app.route("/blog/blog-details/")
def blog_details():
    return render_template("blog-details.html")

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        

        msg = Message(subject,
                      sender=email,
                      recipients=[app.config['MAIL_USERNAME']])  # envoie à toi-même
        msg.body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        mail.send(msg)
        return 'OK'
    except Exception as e:
        lg.warning(f"Erreur lors de l'envoi de l'email : {e}")
        
        return str(e), 500


# if __name__ == "__main__":
#     app.run()
