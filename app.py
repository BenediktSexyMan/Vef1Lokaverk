import os
from bottle import *

@route("/")
def home():
  return "Benedikt er kominn á Heroku"

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=os.environ.get("PORT"))
else:
    run()
