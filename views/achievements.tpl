<!DOCTYPE HTML>
<html>
    <head>
        <link href="/static/achievestyle.css" rel="stylesheet">
    </head>
    <body>
        <h1 class="center">Achievements</h1>
        <div class="box">
            <div class="achievebox">
                <h2>AchievementBox1</h2>
                <h3 class="center">Description</h3>
            </div>
            <div class="achievebox">
                <h2>AchievementBox2</h2>
                <h3 class="center">Description</h3>
            </div>
            <div class="achievebox">
                <h2>AchievementBox3</h2>
                <h3 class="center">Description</h3>
            </div>
            % for x in user.achievements():
            <div class="achievebox">
                <h2>{{x.name() }}</h2>
                <h3 class="center"> {{x.descr()}}</h3>
            </div>
            % end
        </div>
    </body>
</html>