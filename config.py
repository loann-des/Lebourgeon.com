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