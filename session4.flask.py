from flask import Flask , render_template

app = Flask("Test")


@app.route("/")
def default():
    m = "Welcome to my page"
    return render_template("index.html", message=m)

@app.route("/<vistor>")
def hello(vistor):
    m = "Welcome to my page:" + vistor.title()
    return render_template("index.html", message=m)
    #return "hello"



@app.route("/welcome")
def welcome():
    return "Hello welcome to my page"

@app.route("/gen", methods=["POST"])
def welcome():
    return "Hello welcome to my page"


app.run()
