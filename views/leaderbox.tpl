<!DOCTYPE html>
<html>
    <head>
        <link href="./static/leaderboxes.css" type="text/css" rel="stylesheet">
        <meta charset="UTF-8">
        <script src="./static/p5.js" type="text/javascript"></script>
        <script src="./static/p5.dom.js" type="text/javascript"></script>
        <script src="./static/p5.sound.js" type="text/javascript"></script>
        <script src="https://unpkg.com/vue"></script>

    </head>
    <body onload="refInfo()">
        <!--<div class="oneliner">
            <h1 class="object">#1</h1>
            <h2 class="object">David</h2>
            <h2 class="object">4000G</h2>
            <h2 class="object">22 armor</h2>
            <h2 class="object">49230G Total</h2>
            <h2 class="object">182 Treasures found</h2>
            <hr>
        </div>-->
        <div  id="lister" style="display: none;">
            <div v-for='x in top' style="display: flex; justify-content: space-around;">
                <p>{{x.name}}</p>
                <p>{{x.gold}}</p>
                <p>{{["Alive", "Dead"][Number(x.dead)]}}</p>
                <p>{{x.score}}</p>
            </div>
        </div>
        <script>
            var lister = null;
            function refInfo() {
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && this.status == 200) {
                        console.log(xhttp.responseText);
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
                setInterval(refInfo, 15000);
            }
        </script>
    </body>
</html>
