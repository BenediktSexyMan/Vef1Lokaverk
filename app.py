import os
import sys
import random
import re
import json
from time import time as epoch
from bottle import *
from pymysql import *

def indexOfNth(container, elem = " ", nth = 1):
    if nth == 0:
        return 0
    elif nth == "last":
        occ = -1
        for i, x in enumerate(container):
            if x == elem:
                occ = i
        return occ
    else:
        occ = 0
        for i, x in enumerate(container):
            if x == elem:
                occ += 1
            if occ == nth:
                return i
        if occ < nth:
            return len(container) - 1

def sanitize(inputstr):
    sanitized = inputstr
    badstrings = [
        ';',
        '$',
        '&&',
        '../',
        '<',
        '>',
        '%3C',
        '%3E',
        '\'',
        '--',
        '1,2',
        '\x00',
        '`',
        '(',
        ')',
        'file://',
        'input://'
    ]
    for badstr in badstrings:
        if badstr in sanitized:
            sanitized = sanitized.replace(badstr, '')
    return sanitized

conn = connect(host='tsuts.tskoli.is', user='1311992289', passwd='mypassword', db='1311992289_vef1lokaverk')

users  = {"users"  : {}}

class User: # creates user
    def __init__(self, ID, name, profile="/static/android-icon-192x192.png", descr=None, chieves=None):
        self.__ID      = ID
        self.__name    = name
        self.__pro     = profile
        self.__descr   = "" if descr   is None else descr
        self.__chieves = [] if chieves is None else chieves
    def ID(self):
        return self.__ID
    def name(self, new_name=None):
        self.__name = self.__name if new_name is None else new_name
        return self.__name
    def profile(self, new_profile=None):
        self.__pro = self.__pro if new_profile is None else new_profile
        return self.__pro
    def descr(self, new_descr=None):
        self.__descr = self.__descr if new_descr is None else new_descr
        return self.__descr
    def achievements(self, new_chieves=None):
        self.__chieves = self.__chieves if new_chieves is None else new_chieves
        return self.__chieves
    def addAchievement(self, new_chieve):
        self.__chieves.append(new_chieve)
    __repr__ = __str__ = lambda self: "User " + self.__name

class UserEvent: # parent class for submissions
    def __init__(self, ID):
        self.__ID = ID
    def ID(self):
        return self.__ID

class Achieve(UserEvent): #creates achievements
    def __init__(self, ID, name, descr = None, funct = None):
        UserEvent.__init__(self, ID)
        self.__name  = name
        self.__descr = "" if descr is None else descr
        self.__func = funct
    def func(self, user):
        return self.__func(user)
    def name(self):
        return self.__name
    def descr(self):
        return self.__descr
    __repr__ = __str__ = lambda self: "Achievement " + self.__name

class Submission(UserEvent): # collects information for various things
    def __init__(self, ID, userID, gold, wins, defe, dead, score, head, chest, lower, dmg, block, clicks, rounds):
        UserEvent.__init__(self, ID)
        self.__gold   = gold
        self.__wins   = wins
        self.__defe   = defe
        self.__dead   = dead
        self.__score  = score
        self.__user   = userID
        self.__head   = head
        self.__chest  = chest
        self.__lower  = lower
        self.__dmg    = dmg
        self.__block  = block
        self.__clicks = clicks
        self.__rounds = rounds
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
    def head(self):
        return self.__head
    def chest(self):
        return self.__chest
    def lower(self):
        return self.__lower
    def dmg(self):
        return self.__dmg
    def block(self):
        return self.__block
    def clicks(self):
        return self.__clicks
    def rounds(self):
        return self.__rounds
    def user(self):
        return self.__user
    __repr__ = __str__ = lambda self: "Submission " + users["users"][self.user()].name() + " " + str(self.__score)

events = {"achievs": {
    "ONE": Achieve(
        "ONE",
        "Registered Submitter",
        "Hey, you submitted a score!... Coooooool!",
        lambda user: len(list(filter(lambda x: x.user() == user, events["submiss"]))) > 0 # submit a score
    ),
    "TWO": Achieve(
        "TWO",
        "You've Got Gold",
        "Check your inbox",
        lambda user: sum([y.gold() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) > 0 # fá meira en 0 gold
    ),
    "THREE": Achieve(
        "THREE",
        "You've Got clothes",
        "Your adventure is only beginning!",
        lambda user: sum([y.defe() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) > 0 # fá 1 armor
    ),
    "FOUR": Achieve(
        "FOUR",
        "I made it mum",
        "You got a submission on the leaderboard!!!",
        lambda user: len(list(filter(lambda x: x.user() == user,sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 10)]))) > 0 # eitt top 10 score
    ),
    "FIVE": Achieve(
        "FIVE",
        "Top Three",
        "Hope you enjoyed the Paralympics :)",
        lambda user: len(list(filter(lambda x: x.user() == user,sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 3)]))) > 0 # eitt top 3 score
    ),
    "SIX": Achieve(
        "SIX",
        "#1",
        "#1 Baby!",
        lambda user: len(list(filter(lambda x: x.user() == user,sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 1)]))) > 0 # fyrsta sæti á leaderboards
    ),
    "SEVEN": Achieve(
        "SEVEN",
        "You've Got Your First Paycheck",
        "Check your brand new yacht, cus you've got 2500 gold",
        lambda user: sum([y.gold() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 2500 # 2500 gold
    ),
    "EIGHT": Achieve(
        "EIGHT",
        "You've Got Rich",
        "Check your Panama, cus you've got 5000 gold",
        lambda user: sum([y.gold() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 5000 # 5000 gold
    ),
    "NINE": Achieve(
        "NINE",
        "You've Got Riches",
        "Check your Privilige, cus you've got 10000 gold",
        lambda user: sum([y.gold() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 10000 # 10000 gold
    ),
    "TEN": Achieve(
        "TEN",
        "Newbie",
        "Get a total score of 5000",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 5000 # 5k score total
    ),
    "ELEVEN": Achieve(
        "ELEVEN",
        "Beginner",
        "Get a total score of 10000",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 10000 # 10k score total
    ),
    "TWELVE": Achieve(
        "TWELVE",
        "Average Joe",
        "Get a total score of 100000",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 100000 # 100k score total
    ),
    "THIRTEEN": Achieve(
        "THIRTEEN",
        "Worthless Millionaire",
        "You now posess a total of 1 million points! Too bad they can't be used anywhere",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 1000000 # 1m score total
    ),
    "FOURTEEN": Achieve(
        "FOURTEEN",
        "X Factor",
        "Get a total score of 10!",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 3628800 # 10! score total
    ),
    "FIFTEEN": Achieve(
        "FIFTEEN",
        "Carpal Tunnel",
        "Get a total score of 10 million!",
        lambda user: sum([y.score() for y in list(filter(lambda x: x.user() == user, events["submiss"]))]) >= 10000000 # 10m score total
    ),
    "SIXTEEN": Achieve(
        "SIXTEEN",
        "Golden Helmet",
        "by collecting 10 defence worh of head armor pieces you were able to stitch them together into a cool golden helmet!",
        lambda user: list(filter(lambda x: user == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.head(), reverse=True)]))[0].head() >= 10 # 10 head armor í einum leik
    ),
    "SEVENTEEN": Achieve(
        "SEVENTEEN",
        "Golden Chestplate",
        "with 10 defence worth of chestplates you now have golden moobs!",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.chest(), reverse=True)]))[0].chest() >= 10 # 10 body armor í einum leik
    ),
    "EIGHTEEN": Achieve(
        "EIGHTEEN",
        "Golden Pants",
        "Your pants have been upgraded to Golden by collecting 10 defence worth of pants!",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.lower(), reverse=True)]))[0].lower() >= 10 # 10 lower body armor í einum leik
    ),
    "NINETEEN": Achieve(
        "NINETEEN",
        "Vagabond",
        "you got 10k points in a single run!",
        lambda user: list(filter(lambda x: user == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)]))[0].score() >= 10000 #10k points í einu
    ),
    "TWENTY": Achieve(
        "TWENTY",
        "Adventurer",
        "you got 100k points in a single run!",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)]))[0].score() >= 100000 #100k points í einu
    ),
    "TWENTYONE": Achieve(
        "TWENTYONE",
        "20 Year MMORPG Veteran",
        "you got 1 million points in a single run!",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)]))[0].score() >= 1000000 #1m points í einu
    ),
    "TWENTYTWO": Achieve(
        "TWENTYTWO",
        "Golden Mansion",
        "Collect 1000 gold in a single run",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].gold() >= 1000 # 1k gold í einu
    ),
    "TWENTYTHREE": Achieve(
        "TWENTYTHREE",
        "Golden Castle",
        "Collect 2000 gold in a single run",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].gold() >= 2000 # 2k gold í einu
    ),
    "TWENTYFOUR": Achieve(
        "TWENTYFOUR",
        "Golden White House",
        "Collect 3000 gold in a single run",
        lambda user: list(filter(lambda x: user == x.user(),[y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].gold() >= 3000 # 3k gold í einu
    )



}, "submiss": []}

def rows(cur):
    return [x for x in cur]

def updateTop(): # updates the JSON file for leaderboard
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

def updateUsers(): # updates JSON for users
    data = {"users": [], "submiss": []}
    for x in list(users["users"].values()):
        data["users"].append({
            "ID": x.ID(),
            "name": x.name(),
            "PPicFile": x.profile(),
            "descr": x.descr(),
            "chieves": [[y.name(), y.descr()] for y in x.achievements()]
        })
    for x in events["submiss"]:
        data["submiss"].append({
            "user": x.user(),
            "score": x.score(),
            "submiss": "Submission " + str(x.score())
        })
    with open("./static/users.json", "w") as f:
        f.truncate()
        json.dump(data, f)

with conn.cursor() as cur: # syncs local data with database on run
    cur.execute("SELECT ID, name, PPicFile, descr, chieves FROM users")
    for x in cur:
        users["users"][int(x[0])] = User(int(x[0]), str(x[1]), str(x[2]), str(x[3]), (list(filter(lambda x: x is not None, [events["achievs"][y] if y != "" and y is not None else None for y in x[4].split(" ")])) if x[4] != "" else None)) # creates user
    data = {"users": []}
    for x in list(users["users"].values()):
        data["users"].append({
            "ID"      : x.ID(),
            "name"    : x.name(),
            "PPicFile": x.profile(),
            "descr"   : x.descr(),
            "chieves" : [[y.name(), y.descr()] for y in x.achievements()]
        })
    with open("./static/users.json", "w") as f:
        f.truncate()
        json.dump(data, f)
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
                int(x[5]),
                int(x[6]),
                int(x[7]),
                int(x[8]),
                int(x[9]),
                int(x[10]),
                int(x[11]),
                int(x[12]),
            )
        )
    updateUsers()
    data = {"top": []}
    cur.execute("SELECT users.name, submiss.gold, submiss.wins, submiss.def, submiss.dead, submiss.score FROM submiss JOIN users ON users.ID = submiss.userID ORDER BY submiss.score DESC LIMIT 10")
    ans = rows(cur)
    for x in ans:
        data["top"].append(
            {
                "name": str(x[0]),
                "gold": str(x[1]),
                "wins": str(x[2]),
                "def": str(x[3]),
                "dead": str(x[4]),
                "score": str(x[5])
            }
        )
    with open("./static/top.json", "w") as f:
        f.truncate()
        json.dump(data, f)

@route("/static/<filename>") #css stuff
def static_skrar(filename):
    return static_file(filename, root="./static")

@route("/") #home page if logged in, else login page
def home():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            return template("Main.tpl", ch=users["users"][int(user_cookie)].achievements())
        else:
            redirect("/process")
    else:
        return template("unlogged.tpl", logmsg=None, sigmsg=None)

@route("/", method="POST") #submits login
def home2():
    lvs = request.forms.get("LvS")
    if lvs == "login":
        with conn.cursor() as cur:
            cur.execute("SELECT users.ID FROM users WHERE name='" + request.forms.get("username") + "';")
            ans = rows(cur)
            if len(ans):
                cur.execute("SELECT users.ID FROM users WHERE password='" + request.forms.get("password") + "' and name = '" + request.forms.get("username") + "';")
                ans = rows(cur)
                if len(ans):
                    response.set_cookie("user", str(ans[0][0]))  # , secret="SuckMyTCP/IPv4"
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
                return template("unlogged", logmsg=None, sigmsg="User already exists")
            else:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO users(name, password) VALUES ('" + name + "', '" + passw + "');")
                    conn.commit()
                users["users"][len(users["users"]) + 1] = User(len(users["users"]) + 1, name)
                updateUsers()
                response.set_cookie("user", str(len(users["users"])))  # , secret="SuckMyTCP/IPv4"
                redirect("/")
    else:
        redirect("/")

@route("/game") # game
def game():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            return template("extra.tpl")
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/game", method="POST") # game submission
def game2():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            gold   = request.get_cookie("gold")
            dead   = request.get_cookie("dead")
            wins   = request.get_cookie("wins")
            defe   = request.get_cookie("def" )
            score  = int(((int(gold)/2)*(int(wins)/2)*[int(defe)/2,1][int(defe)==0])/[1,2][int(dead)])
            head   = request.get_cookie("head")
            chest  = request.get_cookie("chest")
            lower  = request.get_cookie("lower")
            dmg    = request.get_cookie("dmg")
            block  = request.get_cookie("block")
            clicks = request.get_cookie("clicks")
            rounds = request.get_cookie("rounds")
            with conn.cursor() as cur:
                cur.execute("INSERT INTO submiss(gold, wins, def, dead, score, userID, head, chest, lower, dmg, blockd, clicks, rounds) VALUES (" + str(gold) + "," + str(wins) + "," + str(defe) + "," + str(dead) + "," + str(score) + "," + str(user_cookie) + "," +  str(head) + "," + str(chest) + "," + str(lower) + "," + str(dmg) + "," + str(block) + "," + str(clicks) + "," + str(rounds) + ");")
                conn.commit()
                events["submiss"].append(Submission(
                    len(events["submiss"]) + 1,
                    int(user_cookie),
                    int(gold),
                    int(wins),
                    int(defe),
                    int(dead),
                    int(score),
                    int(head),
                    int(chest),
                    int(lower),
                    int(dmg),
                    int(block),
                    int(clicks),
                    int(rounds)
                ))
                updateUsers()
                updateTop()
                for x in list(events["achievs"].values()): # updates achievements on submissions
                    if x.func(int(user_cookie)) and x not in users["users"][int(user_cookie)].achievements():
                        users["users"][int(user_cookie)].addAchievement(x)
                        cur.execute("UPDATE users SET chieves=CONCAT(chieves,\"" + x.ID() + " " + "\") WHERE ID=" + str(user_cookie) + ";")
                        conn.commit()
                updateUsers()
            return template("extra.tpl")
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/reallylongandununderstandablelinktotheuser") # iframed userpage, we want to make sure you never find this page outside the iframe for your protection, trust me
def user():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            with open("./views/mainuser.tpl", "r") as f:
                return f.read()
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/user") # redirects to userpage
def user():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            redirect("/u")
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/u/<username>") # dynamic route
def userpage(username):
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            if username.lower() in list(map(lambda x: x.lower(), [x.name() for x in users["users"].values()])):
                return template("userpage.tpl", user=list(filter(lambda x: x.name().lower() == username.lower(), list(users["users"].values())))[0], events=events)
            else:
                return template("404.tpl")
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/u") # redirects to your own user
def userpageredirect():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            username=users["users"][int(user_cookie)].name()
            redirect("/u/"+username)
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/useredit") # edit user page
def userpageeditor():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            return template('useredit.tpl', user=users["users"][int(user_cookie)], events=events)
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/save", method="POST") # save changes to user info
def save():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            name = request.forms.get("name")
            if name in [x.name() for x in list(users["users"].values())] and name != users["users"][int(user_cookie)].name(): # If the user tries to update his name to an already existing name
                return "<h1>Username already exists<br><a href=\"/useredit\">TRY AGAIN</a></h1>"
            users["users"][int(user_cookie)].name(name)
            desc = request.forms.get("desc")
            if not len(re.findall("^[^#*<>\"'{}\[\];]+$", desc)) and len(desc) != 0: #anti xss attack regex
                desc = sanitize(desc)
                return desc + "  ? Did you really think that was going to work?"
            users["users"][int(user_cookie)].descr(desc)
            img = request.files.get("imageFile")
            if img is not None: # Ef notandi er að uppfæra profile myndina sína
                if users["users"][int(user_cookie)].profile() != "/static/android-icon-192x192.png": # Tries to delete the previous profile picture if it is not the default
                    try:
                        os.remove("." + users["users"][int(user_cookie)].profile())
                    except: pass
                img.filename = str(epoch()) + img.filename[indexOfNth(img.filename, ".", "last"):] # Changes filename to seconds from epoch
                users["users"][int(user_cookie)].profile("/static/" + img.filename) # Updates the user
                img.save("./static") # Saves the picture
            with conn.cursor() as cur: # Updates the database
                cur.execute(
                    "UPDATE users SET name = \"" \
                    + users["users"][int(user_cookie)].name() \
                    + "\", PPicFile = \""  + users["users"][int(user_cookie)].profile() \
                    + "\", descr = \"" + users["users"][int(user_cookie)].descr() \
                    + "\" WHERE ID = " + user_cookie + ";"
                )
                conn.commit()
            updateUsers() # Updates the JSON files
            updateTop()   # ----------||----------
            redirect("/u")
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/leaderboards") # leaderboard iframed on website
def leader():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            with open("./views/leaderbox.tpl", "r") as f:
                return f.read()
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/leaderpage") # leaderboard ordered by total score
@route("/leaderpage", method="POST")
def leaderboard():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            page = request.query.get("page")
            if page is None:
                page = 0
            else:
                try:
                    int(page)
                    page = int(page)
                except ValueError:
                    page = 0
            maxPage = len(list(users["users"].values()))//15+(len(list(users["users"].values()))%15!=0)
            if page >= maxPage:
                page = 0
            elif page < 0:
                page = maxPage - 1
            if request.forms.get("posted") is not None:
                redirect("/leaderpage?page=" + str(page))
            return template("leaderboard.tpl", page=page, users=sorted(list(users["users"].values()), key=lambda x: sum([z.score() for z in list(filter(lambda y: x.ID() == y.user(), sorted(events["submiss"], key=lambda y: y.score(), reverse=True)))]), reverse=True)[page*15:((page*15)+15 if (page*15)+15 <= len(list(users["users"].values())) else len(list(users["users"].values())))], submiss=events["submiss"])
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/all") # all submissions ordered
def leaderboards():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            return template("allSubs.tpl", users=users["users"], submiss=events["submiss"])
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/achievements") # achievements page
def chavs():
    user_cookie = request.get_cookie("user")  # , secret="SuckMyTCP/IPv4"
    if user_cookie is not None:
        if int(user_cookie) in users["users"]:
            return template("achievements.tpl", events=events, user=users["users"][int(user_cookie)])
        else:
            redirect("/process")
    else:
        redirect("/")

@route("/process") # deletes user cookie
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

conn.close()