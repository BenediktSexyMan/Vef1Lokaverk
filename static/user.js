function getCookie(key) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + key + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

function findUser(users) {
    for(var i in users.users) {
        if(Number(getCookie("user")) == users.users[i].ID) {
            return users.users[i];
        }
    }
}

function findUserSubmission(users) {
    var user = findUser(users);
    var submissions = [];
    for(var i in users.submiss) {
        if(user.ID == Number(users.submiss[i].user)) {
            submissions.push(users.submiss[i]);
        }
    }
    return submissions;
}

function userRank(users, sub) {
    var user = findUser(users);
    var submissions = sub;
    var best;
    if(submissions.length > 0) {
        best = submissions[0];
    }
    users.submiss.sort(function(a, b) {
        return a.score - b.score;
    })
    users.submiss.reverse();
    for(var i in submissions) {
        if(submissions[i].score > best.score) {
            best = submissions[i];
        }
    }
    console.log(best);
    for(var i in users.submiss) {
        if(users.submiss[i] == best) {
            return Number(i)+1;
        }
    }
}

var lister = null;
function refInfo() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var result = JSON.parse(xhttp.responseText);
            for(var i in result.users) {
                if(result.users[i].descr == "None") {
                    result.users[i].descr = "No description given";
                }
            }
            var sub = findUserSubmission(result);
            sub.reverse();
            console.log("gotten2");
            if(lister === null) {
                select("#userLister").style("display", "block");
                lister = new Vue({
                    el: '#userLister',
                    data: {
                        user: findUser(result),
                        submiss: sub,
                        rank: userRank(result, sub)
                    }
                });
            }
            else {
                lister.user = findUser(result);
                lister.submiss = sub;
                lister.rank = userRank(result, sub);
            }
        }
    };
    xhttp.open("GET", "./static/users.json?dummy=" + Date.now().toString(), true);
    xhttp.send();
}

function setup() {
    createCanvas(0,0);
    setInterval(refInfo, 15000);
}

function draw() {
    if(Number(getCookie("justSubbed2"))) {
        setTimeout(refInfo, 2000);
        setTimeout(refInfo, 6000);
        document.cookie="justSubbed2=0";
    }
}