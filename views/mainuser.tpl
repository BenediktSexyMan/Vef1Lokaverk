<!DOCTYPE html>
<html>
    <head>
        <link href="./static/leaderboxes.css" type="text/css" rel="stylesheet">
        <meta charset="UTF-8">
        <script src="./static/p5.js" type="text/javascript"></script>
        <script src="./static/p5.dom.js" type="text/javascript"></script>
        <script src="./static/p5.sound.js" type="text/javascript"></script>
        <script src="https://unpkg.com/vue"></script>
        <link href="./static/style.css" type="text/css" rel="stylesheet">
    </head>
    <body class="userBody" onload="refInfo()">
        <div class="profile">
             <img class="c bgcolor imgsize" src="cosby.jpg">
             <div class="profinfo c bgcolor">
                 <h1 class="uname">Username</h1>
                 <h3>--------------------------------------------------------------------------------------------</h3>
                 <h3 class="bottom">

                 </h3>
             </div>
        </div>
        <div id="userLister" style="display: none;">
            <div v-for="x in users">
                {{x}}
            </div>
        </div>
        <script src="./static/user.js"></script>
    </body>
</html>