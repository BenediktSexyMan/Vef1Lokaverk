import os
import sys
import json
from bottle import *
from pymysql import *
conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')

def rows(cur):
    return [x for x in cur]

data = None
def updateData():
    with conn.cursor() as cur:
        data = {"top": []}
        cur.execute("SELECT users.name, submiss.gold, submiss.wins, submiss.def, submiss.dead, submiss.score FROM submiss JOIN users ON users.ID = submiss.userID ORDER BY submiss.score DESC LIMIT 10;")
        ans = rows(cur)
        for x in ans:
            data["top"].append(
                {
                    "name"  : str(x[0]),
                    "gold"  : str(x[1]),
                    "wins"  : str(x[2]),
                    "def"   : str(x[3]),
                    "dead"  : str(x[4]),
                    "score" : str(x[5])
                }
            )
        print(data)
        with open("./static/top.json", "w") as f:
            f.truncate()
            json.dump(data, f)
updateData()

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
        with conn.cursor() as cur:
            cur.execute("SELECT ID FROM users;")
            if int(user_cookie) in [x[0] for x in rows(cur)]:
                return template("Main.tpl")
            else:
                redirect("/process")
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
    user_cookie = request.get_cookie("user", secret="SuckMyTCP/IPv4")
    if user_cookie is not None:
        with conn.cursor() as cur:
            cur.execute("SELECT ID FROM users;")
            if int(user_cookie) in [x[0] for x in rows(cur)]:
                return template("extra.tpl")
            else:
                redirect("/process")
    else:
        redirect("/")

@route("/game", method="POST")
def game2():
    user_cookie = request.get_cookie("user", secret="SuckMyTCP/IPv4")
    if user_cookie is not None:
        with conn.cursor() as cur:
            cur.execute("SELECT ID FROM users;")
            if int(user_cookie) in [x[0] for x in rows(cur)]:
                print("sibmitting")
                gold  = request.get_cookie("gold")
                dead  = request.get_cookie("dead")
                wins  = request.get_cookie("wins")
                defe  = request.get_cookie("def" )
                score = ((int(gold)/2)*(int(wins)/2)*(int(defe)/2))/[1,2][dead]
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO submiss(gold, wins, def, dead, score, userID) VALUES (" + str(gold) + "," + str(wins) + "," + str(defe) + "," + str(dead) + "," + str(score) + "," + str(user_cookie) + ");")
                    conn.commit()
                    updateData()
                return template("extra.tpl")
            else:
                redirect("/process")
    else:
        redirect("/")

@route("/user")
def user():
    pass

@route("/leaderboards")
def leader():
    user_cookie = request.get_cookie("user", secret="SuckMyTCP/IPv4")
    if user_cookie is not None:
        with conn.cursor() as cur:
            cur.execute("SELECT ID FROM users;")
            if int(user_cookie) in [x[0] for x in rows(cur)]:
                with open("./views/leaderbox.tpl", "r") as f:
                    return f.read()
            else:
                redirect("/process")
    else:
        redirect("/")

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