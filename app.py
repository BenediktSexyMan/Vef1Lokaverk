import os
from bottle import *
from pymysql import *

@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")

@route("/")
def home():
  return template("Main.tpl")

@route("/game")
def game():
    return template("extra.tpl", gold=None, dead=None)

@route("/game", method="POST")
def game2():
    return template("extra.tpl", gold=request.get_cookie("gold"), dead=request.get_cookie("dead"))



@route("/user")
def user():
    pass

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=os.environ.get("PORT"))
else:
    run(host="localhost",port="8080")