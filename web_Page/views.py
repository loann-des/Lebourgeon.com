from flask import Flask ,render_template, request
from flask_mail import Mail, Message
import logging as lg
from config import config as c

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

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        

        msg = Message(subject,
                      sender=email,
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        mail.send(msg)
        return 'OK'
    except Exception as e:
        lg.warning(f"Erreur lors de l'envoi de l'email : {e}")
        
        return str(e), 500
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    from .models import upload as upd
    if request.method == 'POST' :
        file = request.files['file']
        
        upd(name=file.filename, data=file.read())
        
        return f'Uploded {file.filename}'
    return render_template('upload.html')