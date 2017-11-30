<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="/static/usereditstyle.css">
    </head>
    <body>
        <div class="bgcolor midbox">
            <div class="top">
                <form action="/save" method="post" enctype="multipart/form-data">
                    <div class="profbox">
                        <div>
                            <img class="c bgcolor imgsize" src="{{user.profile()}}">
                            <input type="file" accept="image/*" id="file" name="imageFile">
                        </div>
                        <div>
                            <input pattern="^[^#*<>&quot;'{}\[\];]+$" title="Text may not contain any malicious characters" type="text" name="name" id="Username" class="titlebox" value="{{user.name()}}" required>
                            <h3>------------------------------------------------------------</h3>
                            <h3 class="bottomspace">Rank: {{list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))]))[0][0]+1 if len(list(filter(lambda x: user.ID() == x[1].user(), [[ind, elem] for ind, elem in enumerate(sorted(events["submiss"], key=lambda x: x.score(), reverse=True))])))>0 else "None"}}</h3>
                            <textarea class="textbox" name="desc" id="desc">{{user.descr() if user.descr() != "None" else ""}}</textarea>
                        </div>
                    </div>
                    <input class="submissButt" type="submit" value="Save changes">
                </form>
            </div>
        </div>
    </body>
</html>