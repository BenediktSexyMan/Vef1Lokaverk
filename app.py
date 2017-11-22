import os
import sys
import random
import json
from bottle import *
from pymysql import *


conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')


users  = {"users"  : {}}


class User:
    def __init__(self, ID, name, profile=None, descr=None, chieves=None):
        self.__ID      = ID
        self.__name    = name
        self.__pro     = "./static/NonePro.jpg" if profile is None else profile
        self.__descr   = ""                     if descr   is None else descr
        self.__chieves = []                     if chieves is None else chieves
    def ID(self):
        return self.__ID
    def name(self, new_name=None):
        self.__name = self.__name if new_name is None else new_name
        return self.__name
    def profile(self, new_profile=None):
        self.__pro = self.__pro if new_profile is None else new_profile
    def descr(self, new_descr=None):
        self.__descr = self.__descr if new_descr is None else new_descr
    def achievements(self, new_chieves=None):
        self.__chieves = self.__chieves if new_chieves is None else new_chieves
        return self.__chieves
    def addAchievement(self, new_chieve):
        self.__chieves.append(new_chieve)
    __repr__ = __str__ = lambda self: "User " + self.__name


class UserEvent:
    def __init__(self, ID):
        self.__ID = ID
    def ID(self):
        return self.__ID

class Achieve(UserEvent):
    def __init__(self, ID, name: object, descr = None, funct = None):
        UserEvent.__init__(self, ID)
        self.__name  = name
        self.__descr = "" if descr is None else descr
        self.__func = funct
    def func(self, user):
        return self.__func(self, user)
    def name(self):
        return self.__name
    def descr(self):
        return self.__name
    __repr__ = __str__ = lambda self: "Achievement " + self.__name


class Submission(UserEvent):
    def __init__(self, ID, userID, gold, wins, defe, dead, score):
        UserEvent.__init__(self, ID)
        self.__gold  = gold
        self.__wins  = wins
        self.__defe  = defe
        self.__dead  = dead
        self.__score = score
        self.__user  = userID
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
    def user(self):
        return self.__user
    __repr__ = __str__ = lambda self: "Submission " + users["users"][self.user()].name() + " " + str(self.__score)


events = {"achievs": [
    Achieve(
        1,
        "Registered Submitter",
        "Hey, you submitted a score!... Coooooool!",
        lambda self, user: len(list(filter(lambda x: x.user() == user, events["submiss"]))) > 0
    ),
    Achieve(
        2,
        "You've Got Gold",
        "Check your inbox",
        lambda self, user: sum([y.gold() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) > 0
    ),
    Achieve(
        3,
        "I made it mum",
        "You got a submission on the leaderboard!!!",
        lambda self, user: len(list(filter(lambda x: x.user() == user, sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 10)]))) > 0
    )

], "submiss": []}

def rows(cur):
    return [x for x in cur]


def updateTop():
    data = {"top": []}
    for x in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 10)]:
        data["top"].append(
            {
                "name": users["users"][x.user()].name(),
                "gold": str(x.gold()),
                "wins": str(x.wins()),
                "def": str(x.defe()),
                "dead": str(x.dead()),
                "score": str(x.score())
            }
        )
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
with conn.cursor() as cur:
    data = {"top": []}
    cur.execute("SELECT users.name, submiss.gold, submiss.wins, submiss.def, submiss.dead, submiss.score FROM submiss JOIN users ON users.ID = submiss.userID ORDER BY submiss.score DESC LIMIT 10")
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
    with open("./static/top.json", "w") as f:
        f.truncate()
        json.dump(data, f)
print(users)
print(events)




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
                return template("Main.tpl", ch=users["users"][int(user_cookie)].achievements())
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
                    users["users"][int(rows(cur)[0][0])] = User(int(rows(cur)[0][0]), name)
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
                score = int(((int(gold)/2)*(int(wins)/2)*[int(defe)/2,1][int(defe)==0])/[1,2][int(dead)])
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO submiss(gold, wins, def, dead, score, userID) VALUES (" + str(gold) + "," + str(wins) + "," + str(defe) + "," + str(dead) + "," + str(score) + "," + str(user_cookie) + ");")
                    conn.commit()
                    events["submiss"].append(Submission(
                        len(events["submiss"]) + 1,
                        int(user_cookie),
                        int(gold),
                        int(wins),
                        int(defe),
                        int(dead),
                        int(score)
                    ))
                    updateTop()
                for x in events["achievs"]:
                    print(x, x.func(user_cookie))
                    if x.func(user_cookie) and x not in users["users"][int(user_cookie)].achievements():
                        users["users"][int(user_cookie)].addAchievement(x)
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