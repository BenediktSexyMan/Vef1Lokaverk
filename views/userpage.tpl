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
                        <h2 class="center width50">Armor: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.defe(), reverse=True)]))[0].defe() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.defe(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Rounds: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.rounds(), reverse=True)]))[0].rounds() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.rounds(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Clicks: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.clicks(), reverse=True)]))[0].clicks() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.clicks(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Damage Taken: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.dmg(), reverse=True)]))[0].dmg() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.dmg(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Damage Blocked: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.block(), reverse=True)]))[0].block() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.block(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Head Armor: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.head(), reverse=True)]))[0].head() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.head(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Chest Armor: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.chest(), reverse=True)]))[0].chest() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.chest(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Lower Body Armor: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.lower(), reverse=True)]))[0].lower() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.lower(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Score: {{list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))[0].score() if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.score(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                </div>
                <div class="width50">
                    <h1 class="title center">Total</h1>
                    <div class="childchild">
                        <h2 class="center width50">Gold: {{sum(list(map(lambda x: x.gold(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Armor: {{sum(list(map(lambda x: x.defe(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.defe(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.defe(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Rounds: {{sum(list(map(lambda x: x.rounds(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.rounds(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.rounds(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Clicks: {{sum(list(map(lambda x: x.clicks(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.clicks(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.clicks(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Damage Taken: {{sum(list(map(lambda x: x.dmg(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.dmg(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.dmg(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Damage Blocked: {{sum(list(map(lambda x: x.block(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.block(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.block(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Head Armor: {{sum(list(map(lambda x: x.head(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.head(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.head(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Chest Armor: {{sum(list(map(lambda x: x.chest(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.chest(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.chest(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Lower Body Armor: {{sum(list(map(lambda x: x.lower(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.lower(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.lower(), reverse=True)])))>0 else "None"}}</h2>
                        <h2 class="center width50">Score: {{sum(list(map(lambda x: x.score(), list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)]))))) if len(list(filter(lambda x: user.ID() == x.user(), [y for y in sorted(events["submiss"], key=lambda x: x.gold(), reverse=True)])))>0 else "None"}}</h2>
                    </div>
                    <div class="childchild">
                        <h2 class="center width50">Score submissions: {{len(list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))])))}}</h2>
                        <h2 class="center width50">Leaderboard scores: {{len(list(filter(lambda x: x.user() == user.ID(), sorted(events["submiss"], key=lambda x: x.score(), reverse=True)[:min(len(events["submiss"]), 10)])))}}</h2>
                    </div>
                </div>
            </div>
            <h1 class="center"><a href="/achievements">Achievements</a></h1>
            <!--<div class="no">
            % for x in user.achievements():
                <div style="width:50%;text-align:center;">
                    <h2>{{x.name() }}</h2>
                    <h3> {{x.descr()}}</h3>
                </div>
            % end
            </div>-->
        </div>
    </body>
</html>