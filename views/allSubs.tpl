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
    <body class="leadBody" style="overflow-x: hidden;">
        <table id="lister">
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
                % for x in sorted(submiss, key=lambda y: y.ID(), reverse=True):
                    <tr>
                        <td>
                            {{list(filter(lambda y: y.ID() == x.user(), [users[z] for z in users]))[0].name()}}
                        </td>
                        <td>
                            {{x.gold()}}
                        </td>
                        <td>
                            {{x.defe()}}
                        </td>
                        <td>
                            {{x.wins()}}
                        </td>
                        <td>
                            {{["Alive", "Dead"][int(x.dead())]}}
                        </td>
                        <td>
                            {{x.score()}}
                        </td>
                    </tr>
                % end
            </tbody>
        </table>
        <!--<script src="./static/leaderboard.js"></script>-->
    </body>
</html>
