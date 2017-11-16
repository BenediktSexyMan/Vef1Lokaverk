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
        <script src="./static/leaderboard.js"></script>
    </body>
</html>
