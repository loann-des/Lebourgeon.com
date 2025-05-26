import os
SECRET_KEY = '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

APP_G_ID = 1200420960103822

# Database initialization
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

#configue link and txt
E_MAIL = 'lebourgeon.asso@gmail.com'
E_MAIL_LINK = 'mailto:contact@lebourgeon.asso@gmail.com'
INSTA = 'https://www.instagram.com/lebourgeon_asso/'
TEL = '06 40 90 51 17'
LINKEDIN = ''
ADHESION = 'https://www.helloasso.com/associations/le-bourgeon/adhesions/adhesion'
DONS = 'https://www.helloasso.com/associations/le-bourgeon/formulaires/1'

# Configuration Flask-Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'lebourgeon.asso@gmail.com'        # Ton email
MAIL_PASSWORD = 'liyvniblfckrgqyd'      # Mot de passe d'application (pas ton vrai mot de passe !)
