---
layout: post
title: Nethack FAQ 翻译 [1]
categories:
- 翻译
tags: [game,nethack]
status: publish
type: post
published: true
info: 国信嘉园
comment: 好大的工程
meta: {}
---



刚接触nethack，发现中文方面的东西少的可怜，兴起，打算翻这篇我感觉蛮有意思的FAQ，算是为自己备忘。本人AD&D基础薄弱，所以很多专有名词也就不能强求了。争取定时能够分段更新，不要连这个也太监，那也太没面子了....

** YANFAQ **  

*** 又一份被常常问到的问题(YANFAQ) *** 


收集者: Sascha Wostmann (wostmann@geocities.com)

提问:	rec.games.roguelike.nethack 游戏的爱好者回答:

主要由 Sascha Wostmann 回答

Date: May-06-97Version:

1.2我不打算把所有的Spoiler(nethack攻略类资料的别称）都复制过来，而是尽量在这里把那些在新闻组里被常常提到的问题的答案给出来（这就是所谓的FAQ，不是么？）。我根据问题可能出现的先后时间给它们标上了‘级别’。级别就在每个问题的"Q"之前。如果问题属于上一个版本的新问题，那么我在问题前用*表示，例如*2Q: what is ...有一些答案属于ROT13(译者：我不知道这个是指什么...),所以如果你不想读到这些，将不会显示。你也可以在我的攻略主页上将所有的答案用纯文本的方式下载，因为大部分的编辑器都不支持ROT13。当然，欢迎任何的注释和补充。Happy hacking, Saschawostmann@geocities.com(http://www.geocities.com/TimesSquare/3216/index.html) 感谢在修改这篇FAQ中给我建议的：

Dean Luick (dean@falcon.natinst.com)

Kevin Hugo (hugo@cae.wisc.edu)

还有那些我记不清的人，原谅我：）

* * * 

1Q: 我到哪里下载游戏?




在下列站点你可以找到编译好的游戏，或者源码（部分站点）:

ftp://ftp.uu.net/pub/games/nethack

http://www.win.tue.nl/games/roguelike/nethack/index.html

http://www.eecs.lehigh.edu/~jgt2/NetHack/

http://neylonpc.engin.umich.edu/nethack/

http://blues.helsinki.fi/~vviitane/nhcode.html

* * * 

1Q: 我到哪里去找spoiler和其他信息?




下面的站点提供Spoilers，提示以及各类有关内容：

http://www.geocities.com/TimesSquare/3216/index.html

(spoilers etc.)

http://www.eecs.lehigh.edu/~jgt2/NetHack/


 (spoilers and binaries)

http://neylonpc.engin.umich.edu/nethack/

http://www.rhein-main.de/~ptower/




 (hints etc.)

http://www.rz.tu-ilmenau.de/~wi019/





(Slash 4.1.2-x)

http://members.xoom.com/wac/nethack/





(Slash"em beta)

http://www-personal.engin.umich.edu/~mneylon/nethack/ (spoilers etc.)

http://www.win.tue.nl/games/roguelike/nethack/index.html (anything, but old)

http://users.aol.com/ADOMDev/index.html




(ADOM, a variant)而下面这些可以找到一些附加程序，例如NHSound:

http://www.geocities.com/TimesSquare/3216/index.html

(NH_Alert, MK_Bones)

http://www.hut.fi/~tax/nhsound.html





(NHSound)

http://www.cs.hope.edu/~rvaniwaa/xf86ports.html


(OS/2 Tiles version)

* * * 

1Q: NetHack 可以多用户游戏么?




不行。有不少人尝试将它修改成多用户游戏，但是目前为止还没有人完成（实际上，nethack也还没有完成...）

* * * 

1Q: 我怎样使用图形界面游戏?




从3.2版本开始，nethack就包含了一些图形元素。首先，查看你的文档以确认你的版本是否支持。例如DOS版本。如果你想在DOS下激活图形，你必须修改你的配置文件nethack.cnf并且将#OPTIONS=video:autodetect的注释取消。只需要把前面的#符号删掉。当你再次打开nethack，就会以图形界面的方式进入了。在 Unix版本中，你需要修改win/X11/NetHack.ad文件，该文件中包含了大量的X11（Unix图形驱动）可修改参数。最简单的办法就是将该文件中的内容添加到.Xdefaults文件中。该文件中的一个入口注释句为：
NetHack.tile_file: x11tiles
去掉注释符号，就可以进入图形模式。

* * * 

1Q: 我怎样进入探索模式，这样有什么好处?




探索模式下，你将不会死亡。每当你的hp到0时，你可以通过die" target=_blank)http://www.geocities.com/TimesSquare/3216/index.html感谢在修改这篇FAQ中给我建议的：

Dean Luick (dean@falcon.natinst.com)

Kevin Hugo (hugo@cae.wisc.edu)还有那些我记不清的人，原谅我：）

* * * 

1Q: 我到哪里下载游戏?




在下列站点你可以找到编译好的游戏，或者源码（部分站点）:

ftp://ftp.uu.net/pub/games/nethack

http://www.win.tue.nl/games/roguelike/nethack/index.html

http://www.eecs.lehigh.edu/~jgt2/NetHack/

http://neylonpc.engin.umich.edu/nethack/

http://blues.helsinki.fi/~vviitane/nhcode.html

* * * 

1Q: 我到哪里去找spoiler和其他信息?




下面的站点提供Spoilers，提示以及各类有关内容：

http://www.geocities.com/TimesSquare/3216/index.html

(spoilers etc.)

http://www.eecs.lehigh.edu/~jgt2/NetHack/

 &nbsp<br />;

(spoilers and binaries)

http://neylonpc.engin.umich.edu/nethack/

http://www.rhein-main.de/~ptower/




 (hints etc.)

http://www.rz.tu-ilmenau.de/~wi019/





(Slash 4.1.2-x)

http://members.xoom.com/wac/nethack/





(Slash"em beta)

http://www-personal.engin.umich.edu/~mneylon/nethack/ (spoilers etc.)

http://www.win.tue.nl/games/roguelike/nethack/index.html (anything, but old)

http://users.aol.com/ADOMDev/index.html




(ADOM, a variant)而下面这些可以找到一些附加程序，例如NHSound:

http://www.geocities.com/TimesSquare/3216/index.html

(NH_Alert, MK_Bones)

http://www.hut.fi/~tax/nhsound.html





(NHSound)

http://www.cs.hope.edu/~rvaniwaa/xf86ports.html


(OS/2 Tiles version)

* * * 

1Q: NetHack 可以多用户游戏么?




不行。有不少人尝试将它修改成多用户游戏，但是目前为止还没有人完成（实际上，nethack也还没有完成...）

* * * 

1Q: 我怎样使用图形界面游戏?




从3.2版本开始，nethack就包含了一些图形元素。首先，查看你的文档以确认你的版本是否支持。例如DOS版本。如果你想在DOS下激活图形，你必须修改你的配置文件nethack.cnf并且将#OPTIONS=video:autodetect的注释取消。只需要把前面的#符号删掉。当你再次打开nethack，就会以图形界面的方式进入了。在 Unix版本中，你需要修改win/X11/NetHack.ad文件，该文件中包含了大量的X11（Unix图形驱动）可修改参数。最简单的办法就是将该文件中的内容添加到.Xdefaults文件中。该文件中的一个入口注释句为：
NetHack.tile_file: x11tiles
去掉注释符号，就可以进入图形模式。

* * * 

1Q: 我怎样进入探索模式，这样有什么好处?




探索模式下，你将不会死亡。每当你的hp到0时，你可以通过die\[yn\]?




选择n来继续活下拉。你只需要按X就可以在游戏中进入探索模式，或者用nethack -X来打开游戏，而如果你这样进入，同时还会有一支愿望之杖。但是，你无法进入排行榜记录。

* * * 

1Q: 我怎样进入巫师模式，这样有什么好处?




一般版本下使用nethack -u wizard -D可以进入巫师模式。其他修改版本可能会有不同的方法，例如SLASH是nethack -u wizard -Z。在Unix下，你必须是游戏的编译者才能进入，此时只需要 nethack- D即可。在Mac系统中，你只需要把nethack defaults file从目录中临时拿开，就可以在进入的时候出现选择进入巫师模式的对话框。在巫师模式下，你有许多附加的魔法命令，例如魔法定位，搜索，传送等等。你可以用?




并且选择wizard mode commands来获取帮助。该选项仅在巫师模式下有效。同时，还有许多扩展指令有效，但是他们主要是一些调试工具。在巫师模式下主要的不同是：你可以随心所欲的传送（甚至跨层），可以进行魔法定位，可以许愿（包括各种东西，例如祭坛、陷阱等），可以搜索（就像持有暗门探索杖），而且就像探索模式下，你永生不死。

* * * 

1Q: 我在游戏中系统崩溃，导致我最好的一个角色丢失了。我还有办法找回它么?




也许可以。nethack发布中有一个叫做"recover"的程序，他就是你需要的东西。你的nethack目录里会有几个含有你角色的名字并且用数字作为后缀的文件。你只要输入 recover . (无后缀的文件名) 那么就可以恢复你的档案到你进入当前层的时候。注意，"."是指目录，可能需要更换但是，如果是3.2.1那就没有办法了，因为那个版本中，recover存在一个错误。PS: Mac版本可能用"mrecover"或者"recoer".用法很直接，你打开程序，打开 level 0文件，接下来都是自动恢复了。不幸的是，

过去几个发布版本中的recover都是有问题的。所以还是要经常复制保存你的存档文件。

* * * 

1Q: 我听说过所谓Bone文件，这是什么?




如果你的角色死了，有一定的几率当前层信息会被保存下来。该信息文件就叫做bone文件。当另一个角色进入该层数时，有一定的几率，该层不再随机生成，而是读取bone文件重新加载。那么你可以找到前一次死在这一层的尸体，包括尸体上的道具。但是注意，此时大部分的道具都会处于‘诅咒’状态。

* * * 

1Q: 可是我的win95的版本下从来没有找到过bone文件.对，这可能是因为DOS的3.2.2版中存在一个bug。在我的主页上下载安装MK_BONES来修正这个问题。(你会觉得肚子变饱。)

* * * 

1Q: 我在新闻组里面老读到叫Rodney或者Dudley的名字，他们到底是谁？你游戏的主要敌人是Yendor的巫师，是他偷走了Yendor之符。现在，你试着把Yendor到过来看，那么就是Rodney了，而这也是某些老版本游戏中的缺省角色名字。至于Dudley则是有人把Rodney拼错创造出来的名字，一般就当是别名了。

* * * 

