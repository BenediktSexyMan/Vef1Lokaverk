from os import *
from bottle import *
from pymysql import *
conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')

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

@route("/leaderboards")
def leader():
    return template("leaderbox.tpl")

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=environ.get("PORT"))
else:
    run(host="localhost",port="8080")