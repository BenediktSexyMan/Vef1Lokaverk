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

var lister = null;
function refInfo() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            findUser(JSON.parse(xhttp.responseText));
            console.log("gotten2");
            if(lister === null) {
                select("#userLister").style("display", "block");
                lister = new Vue({
                    el: '#userLister',
                    data: {
                        users: findUser(JSON.parse(xhttp.responseText))
                    }
                });
            }
            else {
                lister.users = findUser(JSON.parse(xhttp.responseText));
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
    if(Number(getCookie("justSubbed"))) {
        setTimeout(refInfo, 2000);
        setTimeout(refInfo, 6000);
        document.cookie="justSubbed=0";
    }
}