<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <script src="./static/p5.js" type="text/javascript"></script>
        <script src="./static/p5.dom.js" type="text/javascript"></script>
        <script src="./static/p5.sound.js" type="text/javascript"></script>
        <script src="https://unpkg.com/vue"></script>
        <link href="./static/editstyleorign.css" type="text/css" rel="stylesheet">
    </head>
    <body class="" onload="refInfo()">
        <div id="userLister">
            <div class="userInfo">
                <div class="infoEl imgEl">
                    <img v-bind:src="user.PPicFile" style="background-color: lightblue; max-width: 100%; max-height:100%;">
                </div>
                <div class="infoEl textEl">
                    <h1 class="infoText">{{user.name}}</h1>
                    <h3 class="infoText">
                        Rank {{rank}}
                    </h3>
                    <p class="infoText">{{user.descr}}</p>
                </div>
                <div class="infoEl userAct">
                    <div class="actions">
                        <h3>Submissions</h3>
                        <div style="border-right: 4px #401F0E solid;" class="entries" v-for="x in submiss">
                            <p>{{x.submiss}}</p>
                        </div>
                    </div>
                    <div class="actions chieves">
                        <h3>Achivements</h3>
                        <div style="border-left: 4px #401F0E solid;" class="entries" v-for="x in user.chieves">
                            <p>{{x[0]}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="./static/user.js"></script>
    </body>
</html>