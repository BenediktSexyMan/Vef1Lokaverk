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
    <body class="leadBody" onload="refInfo()" style="overflow: hidden;">
        <table id="lister" style="display: none;">
            <tbody>
                <tr>
                    <th>
                        Name
                    </th>
                    <th>
                        gold
                    </th>
                    <th>
                        def
                    </th>
                    <th>
                        wins
                    </th>
                    <th>
                        State
                    </th>
                    <th>
                        Score
                    </th>
                </tr>
                <tr v-for='x in top'>
                    <td v-bind:onclick="function() { parent.location.location.href = '/u/' + x.name;}">
                        {{x.name}}
                    </td>
                    <td>
                        {{x.gold}}
                    </td>
                    <td>
                        {{x.def}}
                    </td>
                    <td>
                        {{x.wins}}
                    </td>
                    <td>
                        {{["Alive", "Dead"][Number(x.dead)]}}
                    </td>
                    <td>
                        {{x.score}}
                    </td>
                </tr>
            </tbody>
        </table>
        <script src="./static/leaderboard.js"></script>
    </body>
</html>
