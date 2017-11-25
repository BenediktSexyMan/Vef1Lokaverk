<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <script src="./static/p5.js" type="text/javascript"></script>
        <script src="./static/p5.dom.js" type="text/javascript"></script>
        <script src="./static/p5.sound.js" type="text/javascript"></script>
        <script src="https://unpkg.com/vue"></script>
        <link href="./static/editstyle.css" type="text/css" rel="stylesheet">
    </head>
    <body class="" onload="refInfo()">
        <div id="userLister">
            <div>
                <img v-bind:src="users.PPicFile" style="background-color: lightblue;">
                <div>
                    <h3>{{users.name}}</h3>
                </div>
            </div>
        </div>
        <script src="./static/user.js"></script>
    </body>
</html>