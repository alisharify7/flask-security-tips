import os
import datetime
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_session import Session



class SessionConf:
    # session cookie setting
    SESSION_TYPE = "filesystem" # or redis or other db drivers
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=16)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_NAME = 'session-name'



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret key' or os.urandom(24)
app.secret_key = "Secret_KEY"
csrf = CSRFProtect(app=app)
Session(app=app)

@app.route("/",  methods=["GET"]) 
def index_view_page():
     # index view return Hello World Text
      return render_template("index.html")


@app.route("/post/", methods=["POST"])
def post_view():
    return "csrf token is ok"


if __name__ == "__main__":
    app.run(port=5500) # run flask application 