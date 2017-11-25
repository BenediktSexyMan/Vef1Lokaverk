<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="../static/editstyle.css">
    </head>
    <body>
        <div class="bgcolor midbox">
            <div class="profbox">
                <img class="c bgcolor imgsize" src="{{user.profile()}}">
                <div>
                    <h1 class="nametext">{{user.name()}}</h1>
                    <h3>------------------------------------------------------------</h3>
                    <h3 class="bottomspace">
                        Rank {{list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))]))[0][0]+1 if len(list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))])))>0 else "None"}}
                    </h3>
                    <h3>{{user.descr()}}</h3>
                </div>
            </div>
            <hr><h1 class="center">Stats</h1>
            <div class="statbox">
                <div class="width50">
                    <h1 class="title center">Single Game</h1>
                    <div class="childchild">
                        <h2 class="center width50">Gold: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].gold() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Armor:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Rounds:exist=0</h2>
                        <h2 class="center width50">Clicks:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Damage Taken:exist=0</h2>
                        <h2 class="center width50">Damage Blocked:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Head Armor:exist=0</h2>
                        <h2 class="center width50">Chest Armor:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Lower Body Armor:exist=0</h2>
                        <h2 class="center width50">Score: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].score() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                </div>
                <div class="width50">
                    <h1 class="title center">Total</h1>
                    <div class="childchild">
                        <h2 class="center width50">Gold: {{sum(list(map(lambda x: x.gold(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Armor:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Rounds:exist=0</h2>
                        <h2 class="center width50">Clicks:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Damage Taken:exist=0</h2>
                        <h2 class="center width50">Damage Blocked:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Head Armor:exist=0</h2>
                        <h2 class="center width50">Chest Armor:exist=0</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Lower Body Armor:exist=0</h2>
                        <h2 class="center width50">Score: {{sum(list(map(lambda x: x.score(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Score submissions: {{len(list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))])))}}</h2>
                        <h2 class="center width50">Leaderboard scores: {{len(list(filter(lambda x: x.user() == user.ID(), sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 10)])))}}</h2>
                    </div>
                </div>
            </div>
            <h1 class="center">Achievements</h1>
            % for x in user.achievements():
            <div class="childchild">
                <div class="center width50">
                <h2>{{x.name() }}</h2>
                <h3> {{x.descr()}}</h3>
                </div>
            </div>
            % end
        </div>
    </body>
</html>