import os
from bottle import *
from pymysql import *

@route("/")
def home():
  return template('Main.tpl')

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=os.environ.get("PORT"))
else:
    run()
