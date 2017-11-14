Array.prototype.sum = function() {return [].reduce.call(this, (a,i) => a+i, 0);}

function choice(choices) {
  return choices[Math.floor(Math.random()*choices.length)];
}

function Armor(name, def){
    this.name = name;
    this.def  = def;
}

function Player(hp){
    this.hp  = hp;
    this.arm = {
        head : new Armor("Nothing"        , 0),
        torso: new Armor("Dirty Rags"     , 0),
        legs : new Armor("Dirty Loincloth", 0)
    };
}

var t;
var ot;
var butt1;
var butt2;
var butt3;
var p1;
var p2;
var p3;
var p4;
var bw;
var bh;
var ph;
var timeOffset          = 5000;
var currentTimeOffset   = timeOffset;
var player              = new Player(10);
var gold                = 0;
var progress            = 0;
var progressRate        = 25;
var currentProgressRate = progressRate;
var playin              = 0;
var bfd                 = 10;
var pfd                 = 20;
var fd                  = bfd;
var FD                  = 26;
var phd                 = 6;
var bwd                 = 2;
var bhd                 = 4;
var turns               = [0,0];
var names               = [
    ["Legandary"     , "Awesome"       , "Historic", "Mythical"   , "Fabled"    ],
    ["Melon"         , "Fez"           , "Sombrero", "Bucket"     , "Cone"      ],
    ["Breast Implant", "Nipple tassels", "Poncho"  , "Plastic Bag", "Chestplate"],
    ["Yoga Pants"    , "Slippers"      , "Jeans"   , "Jordans"    , "Undies"    ]
];

function setup() {
    createCanvas(windowWidth,windowHeight);
    frameRate   (60);
    bw  = width /bwd;
    bh  = height/bhd;
    ph  = height/phd;
    p1 = createP(player.arm.head .name + " " + player.arm.head .def + " def");
    p2 = createP(player.arm.torso.name + " " + player.arm.torso.def + " def");
    p3 = createP(player.arm.legs .name + " " + player.arm.legs .def + " def");
    p4 = createP("Gold 0" + " HP " + player.hp);
    document.cookie = "gold=0";
    document.cookie = "dead=0";
    if(true){
    butt1=createDiv    ("<p>Find Treasure   </p>"                                             );
    butt2=createDiv    ("<p>PRESS           </p>"                                             );
    butt3=createDiv    ("<p>Insert Gold Here</p>"                                             );
    butt4=createElement("form","<input class=\"submitter\" type=\"submit\">"                  );
    butt1.mousePressed (pressed                                                               );
    butt2.mousePressed (pressed2                                                              );
    butt3.mousePressed (pressed3                                                              );
    butt1.mouseReleased(released                                                              );
    butt2.mouseReleased(released2                                                             );
    butt3.mouseReleased(released3                                                             );
    butt1.mouseOver    (moused                                                                );
    butt2.mouseOver    (moused2                                                               );
    butt3.mouseOver    (moused3                                                               );
    butt1.mouseClicked (clicked                                                               );
    butt2.mouseClicked (clicked2                                                              );
    butt3.mouseClicked (clicked3                                                              );
    butt1.style        ("position"        , "absolute"                                        );
    butt2.style        ("position"        , "absolute"                                        );
    butt3.style        ("position"        , "absolute"                                        );
    butt4.style        ("position"        , "absolute"                                        );
    p1   .style        ("position"        , "absolute"                                        );
    p2   .style        ("position"        , "absolute"                                        );
    p3   .style        ("position"        , "absolute"                                        );
    p4   .style        ("position"        , "absolute"                                        );
    butt1.style        ("background-color", "gray"                                            );
    butt2.style        ("background-color", "gray"                                            );
    butt3.style        ("background-color", "gray"                                            );
    butt1.style        ("text-align"      , "center"                                          );
    butt2.style        ("text-align"      , "center"                                          );
    butt3.style        ("text-align"      , "center"                                          );
    butt1.style        ("display"         , "flex"                                            );
    butt2.style        ("display"         , "none"                                            );
    butt3.style        ("display"         , "none"                                            );
    butt1.style        ("flex-flow"       , "column"                                          );
    butt2.style        ("flex-flow"       , "column"                                          );
    butt3.style        ("flex-flow"       , "column"                                          );
    butt1.style        ("justify-content" , "center"                                          );
    butt2.style        ("justify-content" , "center"                                          );
    butt3.style        ("justify-content" , "center"                                          );
    butt1.style        ("width"           , bw                                .toString()+"px");
    butt2.style        ("width"           , bw                                .toString()+"px");
    butt3.style        ("width"           , bw                                .toString()+"px");
    butt4.style        ("width"           , bw                                .toString()+"px");
    butt1.style        ("height"          , bh                                .toString()+"px");
    butt2.style        ("height"          , bh                                .toString()+"px");
    butt3.style        ("height"          , bh                                .toString()+"px");
    butt4.style        ("height"          , bh                                .toString()+"px");
    butt1.style        ("left"            , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt2.style        ("left"            , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt3.style        ("left"            , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt4.style        ("left"            , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt1.style        ("font-size"       , (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt2.style        ("font-size"       , (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt3.style        ("font-size"       , (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt1.style        ("top"             , ((height/(bhd*2))*(bhd-1))        .toString()+"px");
    butt2.style        ("top"             , ((height/(bhd*2))*(bhd-1))        .toString()+"px");
    p1   .style        ("font-size"       , (min(windowWidth,windowHeight)/FD).toString()+"px");
    p2   .style        ("font-size"       , (min(windowWidth,windowHeight)/FD).toString()+"px");
    p3   .style        ("font-size"       , (min(windowWidth,windowHeight)/FD).toString()+"px");
    p1   .style        ("top"             ,  height/10                        .toString()+"px");
    p2   .style        ("top"             , (height/10)*4                     .toString()+"px");
    p3   .style        ("top"             , (height/10)*7                     .toString()+"px");
    p4   .style        ("font-size"       , (min(windowWidth,windowHeight)/20).toString()+"px");
    p4   .style        ("top"             , "0"                                               );
    butt3.style        ("bottom"          , "0"                                               );
    butt4.style        ("bottom"          , "0"                                               );
    butt4.attribute    ("action"          , "http:\\\\www.vaktin.is"                          );
    butt4.attribute    ("class"           , "former"                                          );
    }
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    bw  = width /bwd;
    bh  = height/bhd;
    ph  = height/phd;
    butt1.style("width"    , bw                                .toString()+"px");
    butt2.style("width"    , bw                                .toString()+"px");
    butt3.style("width"    , bw                                .toString()+"px");
    butt4.style("width"    , bw                                .toString()+"px");
    butt1.style("height"   , bh                                .toString()+"px");
    butt2.style("height"   , bh                                .toString()+"px");
    butt3.style("height"   , bh                                .toString()+"px");
    butt4.style("height"   , bh                                .toString()+"px");
    butt1.style("left"     , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt2.style("left"     , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt3.style("left"     , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt4.style("left"     , (((width-bw)/2)+bw*(bwd/4))       .toString()+"px");
    butt1.style("font-size", (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt2.style("font-size", (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt3.style("font-size", (min(windowWidth,windowHeight)/fd).toString()+"px");
    butt1.style("top"      , ((height/(bhd*2))*(bhd-1))        .toString()+"px");
    butt2.style("top"      , ((height/(bhd*2))*(bhd-1))        .toString()+"px");
    p1   .style("font-size", (min(windowWidth,windowHeight)/FD).toString()+"px");
    p2   .style("font-size", (min(windowWidth,windowHeight)/FD).toString()+"px");
    p3   .style("font-size", (min(windowWidth,windowHeight)/FD).toString()+"px");
    p1   .style("top"      ,  height/10                        .toString()+"px");
    p2   .style("top"      , (height/10)*4                     .toString()+"px");
    p3   .style("top"      , (height/10)*7                     .toString()+"px");
    p4   .style("font-size", (min(windowWidth,windowHeight)/20).toString()+"px");

}

pressed   = function(){butt1.style("background-color", "lightgray");};
pressed2  = function(){butt2.style("background-color", "lightgray");};
pressed3  = function(){butt3.style("background-color", "lightgray");};
released  = function(){butt1.style("background-color", "gray"     );};
released2 = function(){butt2.style("background-color", "gray"     );};
released3 = function(){butt3.style("background-color", "gray"     );};
moused    = function(){butt1.style("cursor"          , "pointer"  );};
moused2   = function(){butt2.style("cursor"          , "pointer"  );};
moused3   = function(){butt3.style("cursor"          , "pointer"  );};
clicked   = function(){ot=Date.now();t=ot+currentTimeOffset;playin=1;butt1.style("display","none");butt2.style("display","flex");butt4.style("display","none");};
clicked2  = function(){progress+=currentProgressRate};
clicked3  = function(){butt3.style("display","none");butt1.style("display","flex");butt4.style("display","flex");select("#page").style("font-size",(min(windowWidth,windowHeight)/bfd).toString()+"px");fd=bfd;};

function draw() {
    if(0 >= player.hp) {
        butt1.mouseClicked(function(){});
        butt1.style("display", "none");
        document.cookie = "dead=1";
    }
    if(p4.html() != "Gold " + gold.toString() + " HP " + player.hp)
        p4.html("Gold " + gold.toString() + " HP " + player.hp);
    frameRate(60);
    clear();
    if(playin) {
        print("ProgressRate " + currentProgressRate.toString());
        tim = Date.now()
        if(tim<t && progress<100){
            fill(255,0,0);
            rect(width/2, 0,(currentTimeOffset-(t-tim))*(width/(currentTimeOffset*2)), ph);
            fill(0,0,255);
            rect(width/2,ph,map(progress,0,100,0,width/2),ph);
        }
        else {
            print("TimeOffset " + currentTimeOffset.toString());
            fill(255,0,0);
            rect(width/2, 0,(currentTimeOffset-(t-tim))*(width/(currentTimeOffset*2)), ph);
            fill(0,0,255);
            rect(width/2,ph,map(progress,0,100,0,width/2),ph);
            var mess;
            if(progress>=100) {
                turns[0]++;
                if(currentProgressRate > 10) {
                    currentProgressRate-=1;
                }
                if(currentTimeOffset == timeOffset) {
                    currentTimeOffset -= 500;
                }
                else {
                    currentTimeOffset -= floor((timeOffset*25)/(timeOffset-currentTimeOffset))
                }
                print(0.2+((turns[1]-turns[0])/500));
                if(random()>0.3+((turns[1]-turns[0])/500)) {
                    mess  = floor((random()*100000))%99+1;
                    gold += mess;
                    document.cookie = "gold=" + gold.toString();
                    mess  = mess.toString() + " Gold";
                }
                else {
                    var arm = choice(["head","torso","legs"]);
                    var fn  = choice(names[0]);
                    var sn;
                    if(arm == "head" ) {
                        sn = choice(names[1]);
                        player.arm.head  = new Armor(fn+" "+sn, player.arm.head .def + 2);
                    }
                    if(arm == "torso") {
                        sn = choice(names[2]);
                        player.arm.torso = new Armor(fn+" "+sn, player.arm.torso.def + 2);
                    }
                    if(arm == "legs" ) {
                        sn = choice(names[3]);
                        player.arm.legs  = new Armor(fn+" "+sn, player.arm.legs .def + 2);
                    }
                    mess = fn + " " + sn;
                }
            }
            else {
                turns[1]++;
                var subt = 0;
                subt = (floor(turns[0] / 2) + 2) - (player.arm.head.def + player.arm.torso.def + player.arm.legs.def);
                if (subt < 0)
                    subt = 0;
                mess = "Lost " + subt.toString() + " HP";
                player.hp -= subt;
            }
            progress = 0;
            playin   = 0;
            butt3.html("<p>" + mess + "</p>");
            butt2.style("display", "none");
            butt3.style("display", "flex");
            fd=pfd;
            select("#page").style("font-size",(min(windowWidth,windowHeight)/pfd).toString()+"px");
            frameRate(10);
        }
    }
    if(p1.html() != player.arm.head .name + " " + player.arm.head .def + " def")
        p1.html(player.arm.head .name + " " + player.arm.head .def + " def");
    if(p2.html() != player.arm.torso.name + " " + player.arm.torso.def + " def")
        p2.html(player.arm.torso.name + " " + player.arm.torso.def + " def");
    if(p3.html() != player.arm.legs .name + " " + player.arm.legs .def + " def")
        p3.html(player.arm.legs .name + " " + player.arm.legs .def + " def");
    noFill();
    line(width/2,0,width/2,height);
    ellipse((width/2)/2.15,height/8,height/4,height/4);
    rect((width/3)/3,(height-height/3)/2.5,width/4,height/3,width/4,width/4,0,0);
    triangle((width/3)/3,((height-height/3)/2.5)+(height/3)+6,((width/3)/3)+(width/4),((height-height/3)/2.5)+(height/3)+6,(((width/3)/3)+(width/4))/1.5,height-14);
}