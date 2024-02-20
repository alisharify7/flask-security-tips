from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__) 
app.config['SECRET_KEY'] = 'Secret key'
csrf = CSRFProtect(app=app)


@app.route("/",  methods=["GET"]) 
def index_view_page():
     # index view return Hello World Text
      return render_template("index.html")


@app.route("/post/", methods=["POST"])
def post_view():
    return "csrf token is ok"


if __name__ == "__main__":
    app.run(port=5500) # run flask application 