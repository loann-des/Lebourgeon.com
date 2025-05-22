from flask import Flask ,render_template
import config as c

app = Flask(__name__)

# app.config.from_object('config')
# Config options - Make sure you created a 'config.py' file.
app.config.from_object("config")

# To get one variable, tape app.config['MY_VARIABLE']
app.config["SQLALCHEMY_DATABASE_URI"] = c.SQLALCHEMY_DATABASE_URI


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


# if __name__ == "__main__":
#     app.run()
