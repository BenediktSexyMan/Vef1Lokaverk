<!DOCTYPE HTML>
<html>
    <head>
        <link href="/static/leadpagestyle.css" rel="stylesheet">
    </head>
    <body>
        <h1 class="title">Leaderboards</h1>
        <div class="box">
            <h2 class="size1">Rank</h2>
            <h2 class="size2">Max Gold</h2>
            <h2 class="size3">Max Def</h2>
            <h2 class="size4">Max Wins</h2>
            <h2 class="size5">Total Gold</h2>
            <h2 class="size6">Total Score</h2>
        </div>
        % for x, elem in enumerate(users):
            <div class="box">
                <h3 class="size1">#{{(x+1)*((page*15)+1)}} {{elem.name()}}</h3>
                <h3 class="size2">{{list(filter(lambda y: elem.ID() == y.user(), [y for y in sorted(submiss, key=lambda y: y.gold(), reverse=True)]))[0].gold() if len(list(filter(lambda y: elem.ID() == y.user(), [z for z in sorted(submiss, key=lambda y: y.gold(), reverse=True)])))>0 else "None"}}</h3>
                <h3 class="size3">{{list(filter(lambda y: elem.ID() == y.user(), [y for y in sorted(submiss, key=lambda y: y.defe(), reverse=True)]))[0].defe() if len(list(filter(lambda y: elem.ID() == y.user(), [z for z in sorted(submiss, key=lambda y: y.defe(), reverse=True)])))>0 else "None"}}</h3>
                <h3 class="size4">{{list(filter(lambda y: elem.ID() == y.user(), [y for y in sorted(submiss, key=lambda y: y.wins(), reverse=True)]))[0].wins() if len(list(filter(lambda y: elem.ID() == y.user(), [z for z in sorted(submiss, key=lambda y: y.wins(), reverse=True)])))>0 else "None"}}</h3>
                <h3 class="size5">{{sum(list(map(lambda y: y.gold(), list(filter(lambda y: elem.ID() == y.user(), [y for y in sorted(submiss, key=lambda y: y.gold(), reverse=True)]))))) if len(list(filter(lambda y: elem.ID() == y.user(), [z for z in sorted(submiss, key=lambda y: y.gold(), reverse=True)])))>0 else "None"}}</h3>
                <h3 class="size6">{{sum(list(map(lambda y: y.score(), list(filter(lambda y: elem.ID() == y.user(), [y for y in sorted(submiss, key=lambda y: y.gold(), reverse=True)]))))) if len(list(filter(lambda y: elem.ID() == y.user(), [z for z in sorted(submiss, key=lambda y: y.gold(), reverse=True)])))>0 else "None"}}</h3>
            </div>
        % end
    </body>
    <footer>
        <div class="box center">
            <form action="/leaderpage?page={{page-1}}" method="POST">
                <input type="checkbox" name="posted" checked required style="display: none;">
                <input type="submit" value="previous">
            </form>
            <form action="/" method="POST">
                <input type="checkbox" name="posted" checked required style="display: none;">
                <input type="submit" value="Home">
            </form>
            <form action="/leaderpage?page={{page+1}}"  method="POST">
                <input type="checkbox" name="posted" checked required style="display: none;">
                <input type="submit" value="next">
            </form>
        </div>
    </footer>
</html>