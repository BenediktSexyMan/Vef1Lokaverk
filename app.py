import os
from bottle import *
from pymysql import *

@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")

@route("/")
def home():
  return template('extra.tpl')

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=os.environ.get("PORT"))
else:
    run()