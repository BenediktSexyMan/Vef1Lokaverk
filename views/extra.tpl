<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>game</title>
        <script src="./static/p5.js" type="text/javascript"></script>
        <script src="./static/p5.dom.js" type="text/javascript"></script>
        <script src="./static/p5.sound.js" type="text/javascript"></script>
        <script src="./static/sketch.js" type="text/javascript"></script>
    </head>
    <body id="page" style="user-select: none;">
        % if gold is not None:
            <h1>{{gold}}</h1>
        % end
        % if dead is not None:
            <h1>{{dead}}</h1>
        % end
        <style>
            body {
                padding: 0;
                margin: 0;
                overflow: hidden;
                background-color: darkgray;
            }
            canvas {
                vertical-align: top;
            }
            p {
                margin: 0;
            }
            h1 {
                display: none;
            }
            .submitter {
                width: 100%;
                height: 100%;
                border: none;
                padding: 0;
            }
        </style>
    </body>
</html>
