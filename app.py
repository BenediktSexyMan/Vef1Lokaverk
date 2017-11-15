import os
import sys
from bottle import *
from pymysql import *
conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')

def rows(cur):
    return [x for x in cur]

class User:
    def __init__(self, name, profile="./static/NonePro.jpg", descr=""):
        self.__name  = name
        self.__pro   = profile
        self.__descr = descr
    def name(self, new_name=None):
        self.__name = self.__name if new_name is None else new_name
        return self.__name
    def profile(self, new_profile=None):
        self.__pro = self.__pro if new_profile is None else new_profile
    def descr(self, new_descr=None):
        self.__descr = self.__descr if new_descr is None else new_descr
    __repr__ = __str__ = lambda self: "User " + self.__name

class UserEvent:
    def __init__(self, userID):
        self.__user = userID
    def user(self):
        return self.__user

class Achieve(UserEvent):
    def __init__(self, userID, name, descr=""):
        UserEvent.__init__(self, userID)
        self.__name  = name
        self.__descr = descr
    def name(self):
        return self.__name
    def descr(self):
        return self.__name

class Submission(UserEvent):
    def __init__(self, userID, gold, dead):
        UserEvent.__init__(self, userID)
        self.__gold = gold
        self.__dead = dead
    def gold(self):
        return self.__gold
    def dead(self):
        return self.__dead

users = dict()


@route("/static/<filename>")
def static_skrar(filename):
    return static_file(filename, root="./static")

@route("/")
def home():
    user_cookie = request.get_cookie("user", secret="SuckMyTCP/IPv4")
    if user_cookie is not None:
        return template("Main.tpl")
    else:
        return template("unlogged.tpl", logmsg=None, sigmsg=None)

@route("/", method="POST")
def home2():
    lvs = request.forms.get("LvS")
    if lvs == "login":
        with conn.cursor() as cur:
            cur.execute("SELECT users.ID FROM users WHERE name='" + request.forms.get("username") + "';")
            ans = rows(cur)
            if len(ans):
                cur.execute("SELECT users.ID FROM users WHERE password='" + request.forms.get("password") + "';")
                ans = rows(cur)
                if len(ans):
                    response.set_cookie("user", ans[0][0], secret="SuckMyTCP/IPv4")
                    redirect("/")
                else:
                    return template("unlogged.tpl", logmsg="Password is incorrect", sigmsg=None)
            else:
                return template("unlogged", logmsg="User does not exist", sigmsg=None)
    elif lvs == "signup":
        with conn.cursor() as cur:
            name  = request.forms.get("username")
            passw = request.forms.get("password")
            cur.execute("SELECT users.ID FROM users WHERE name='" + request.forms.get("username") + "';")
            ans = rows(cur)
            if len(ans):
                return template("unlogged", logmsg=None, sigmsg="Usser alrady exists")
            else:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO users(name, password) VALUES ('" + name + "', '" + passw + "');")
                    conn.commit()
                    cur.execute("SELECT users.ID FROM users WHERE name='" + name + "';")
                    response.set_cookie("user", rows(cur)[0][0], secret="SuckMyTCP/IPv4")
                    redirect("/")
    else:
        redirect("/")

@route("/game")
def game():
    ''''user_cookie = request.get_cookie("user", secret="SuckMyTCP/IPv4")
    if user_cookie is not None:
        return template("extra.tpl")
    else:
        return template("Main.tpl")  #Mun vera breytt í login/signup síðu'''
    return template("extra.tpl")

@route("/game", method="POST")
def game2():
    return template("extra.tpl")

@route("/user")
def user():
    pass

@route("/leaderboards")
def leader():
    return template("leaderbox.tpl")

@route("/process")
def process():
    try:
        response.delete_cookie("user")
    finally:
        pass
    redirect("/")

if os.environ.get("IS_HEROKU") is not None:
    run(host="0.0.0.0", port=os.environ.get("PORT"))
else:
    run(host="localhost",port="8080")