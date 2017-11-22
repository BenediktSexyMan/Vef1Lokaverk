import os
import sys
import json
from bottle import *
from pymysql import *


conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')


class User:
    def __init__(self, ID, name, profile="./static/NonePro.jpg", descr=""):
        self.__ID      = ID
        self.__name    = name
        self.__pro     = "./static/NonePro.jpg" if profile is None else profile
        self.__descr   = ""                     if descr   is None else descr
    def ID(self):
        return self.__ID
    def name(self, new_name=None):
        self.__name = self.__name if new_name is None else new_name
        return self.__name
    def profile(self, new_profile=None):
        self.__pro = self.__pro if new_profile is None else new_profile
    def descr(self, new_descr=None):
        self.__descr = self.__descr if new_descr is None else new_descr
    __repr__ = __str__ = lambda self: "User " + self.__name


class UserEvent:
    def __init__(self, ID, userID):
        self.__user = userID
    def user(self):
        return self.__user

class Achieve(UserEvent):
    def __init__(self, ID, userID, name, descr=None):
        UserEvent.__init__(self, ID, userID)
        self.__name  = name
        self.__descr = "" if descr is None else descr
    def name(self):
        return self.__name
    def descr(self):
        return self.__name
    __repr__ = __str__ = lambda self: "Achievement " + self.__name


class Submission(UserEvent):
    def __init__(self, ID, userID, gold, wins, defe, dead, score):
        UserEvent.__init__(self, ID, userID)
        self.__gold  = gold
        self.__wins  = wins
        self.__defe  = defe
        self.__dead  = dead
        self.__score = score
    def gold(self):
        return self.__gold
    def wins(self):
        return self.__wins
    def defe(self):
        return self.__defe
    def dead(self):
        return self.__dead
    def score(self):
        return self.__score
    __repr__ = __str__ = lambda self: "Submission " + users["users"][self.user()].name() + " " + str(self.__score)


users  = {"users"  : {}}
events = {"achievs": [], "submiss": []}
with conn.cursor() as cur:
    pass


def rows(cur):
    return [x for x in cur]


def updateTop(data):
    print(data)
    with open("./static/top.json", "w") as f:
        f.truncate()
        json.dump(data, f)


with conn.cursor() as cur:
    cur.execute("SELECT ID, name, PPicFile, descr FROM users")
    for x in cur:
        users["users"][int(x[0])] = User(int(x[0]), str(x[1]), str(x[2]), str(x[3]))
    cur.execute("SELECT * FROM submiss ORDER BY ID ASC")
    for x in cur:
        events["submiss"].append(
            Submission(
                int(x[0]),
                int(x[6]),
                int(x[1]),
                int(x[2]),
                int(x[3]),
                int(x[4]),
                int(x[5])
            )
        )
    cur.execute("SELECT * FROM achievs ORDER BY ID ASC")
    for x in cur:
        events["achievs"].append(
            Achieve(
                int(x[0]),
                int(x[3]),
                int(x[1]),
                int(x[2])
            )
        )
print(users)
print(events)


def updateData():
    with conn.cursor() as cur:
        data = {"top": []}
        cur.execute("SELECT users.name, submiss.gold, submiss.wins, submiss.def, submiss.dead, submiss.score FROM submiss JOIN users ON users.ID = submiss.userID ORDER BY submiss.ID DESC")
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
    updateTop(data)


updateData()



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
                score = ((int(gold)/2)*(int(wins)/2)*[int(defe)/2,1][int(defe)==0])/[1,2][int(dead)]

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