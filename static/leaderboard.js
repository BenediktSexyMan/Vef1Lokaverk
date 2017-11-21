function getCookie(key) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + key + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

var lister = null;
function refInfo() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        console.log("gotten");
            if(lister === null) {
                select("#lister").style("display", "block");
                lister = new Vue({
                    el: '#lister',
                    data: {
                        top: JSON.parse(xhttp.responseText).top
                    }
                });
            }
            else {
                lister.top = JSON.parse(xhttp.responseText).top;
            }
        }
    };
    xhttp.open("GET", "./static/top.json?dummy=" + Date.now().toString(), true);
    xhttp.send();
}

function setup() {
    createCanvas(0,0);
    setInterval(refInfo, 15000);
}

function draw() {
    if(Number(getCookie("justSubbed"))) {
        setTimeout(refInfo, 1000);
        document.cookie="justSubbed=0";
    }
}