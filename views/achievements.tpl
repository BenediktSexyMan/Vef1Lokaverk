<!DOCTYPE HTML>
<html>
    <head>
        <link href="/static/achievestyle.css" rel="stylesheet">
    </head>
    <body>
        <h1 class="center">Achievements</h1>
        <h1 class="center">{{ format((len(user.achievements()) * 100) / len(list(events["achievs"].values())), '.01f') }}%</h1>
        % if len(user.achievements()) == len(list(events["achievs"].values())):
            <h1 class="center">Congratulations!<br>You have earned all of the achievements!</h1>
        % end
        <div class="box">
            % for x in list(events["achievs"].values()):
                % if x in user.achievements():
                    <div class="achieveboxwin">
                        <div class="sendpics">
                            <h2 class="center">{{x.name() }}</h2>
                            <img src="/static/achievement.PNG">
                        </div>
                        <h3 class="center">{{x.descr()}}</h3>
                    </div>
                % else:
                    <div class="achievebox">
                        <h2 class="center">{{x.name() }}</h2>
                        <h3 class="center"> {{x.descr()}}</h3>
                    </div>
                % end
            % end
        </div>
        <a class="sendpics" href="/"><input type="button" value="Home"></a>
    </body>
</html>