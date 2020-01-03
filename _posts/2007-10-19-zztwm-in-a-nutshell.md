---
layout: post
title: '转载: TWM in a nutshell'
categories:
- 技术
tags: [linux]
info: 上海
status: publish
type: post
published: true
meta: {}
---

本文只涉及到TWM的入门级知识，大家都知道很多UNIX下程序的教程都可以写成一本书，在这里我只介绍入门的一些东西，如果本文能帮助某些朋友对TWM有个大致的了解，就算完成它的使命了，其他的复杂部分，就需要自己去探索了。



TWM 是Tab Window Manager for the X Window System的简称，它是一个窗口管理器，初次发布于1988年4月，是个非常容易上手的Window Manager。不像其他的X程序，它没有基于任何GUI组件，而是直接使用的XLib，这样带来的好处就是：小、更方便的配置。所谓窗口管理器，它是一个特殊的程序，它用来给X程序提供诸如：标题的绘制、窗口阴影、窗口图标化、用户自定义宏、鼠标点击、键盘焦点、缩放等功能。



它和 GNOME、KDE不同，不是一个桌面环境(Desktop Enviroment,DE)。那些所谓的桌面环境都会有一个窗口管理器，比如CentOS的GNOME用的就是MetaCity，这些DE集成了大量的应用程序，包括一些非常便利的系统管理工具、实用小工具、游戏等，大大方便了用户。



桌面环境纵有千般好，也会有它的短处，比如：由于它的庞大，在系统启动的时候会显的很慢，其实有很多应用我们都不会用到，这个时候，你可选择只加载一个窗口管理器即可。而且你将会发现，几乎所有的窗口管理器都可以用rc文件来配置，你可以在允许的范围内，任意的配置。比如TWM的配置文件就是.twmrc。它位于用户目录下，在TWM启的时候它会首先从用户的主目录下找这个文件，如果它找不到，TWM就会使用一个系统共用的配置文件，一般情况下它位于： /usr/X11R6/lib/X11/twm/system.twmrc。



为了要启动TWM，而不是GNOME或KDE，我们需要在用户的目录下编辑一个.xinitrc的文件，它的内容如下：



\#!/bin/sh

xclock -geometry 70x70+5+5 &amp;xterm -geometry +200+200 -fn 7x13 -fg gray -bg black &amp;

exec twm

这样，当你在执行startx的时候，就只会启动TWM了。最后一行表示启动TWM，前面的两行表示启动的其他程序，比如 xclock，它是一个时钟程序，它后面的参数表示它启动后所在的位置和大小。需要注意的是，除了最后一行，其他的行要在最后加上后台运行标志，否则后面的程序都没法进行了。除了最后一行，其他的都是可选的，你可以把你常用的一些程序放在exec twm前，这就和Windows下的启动一样。startx后，你将会发现，TWM的启动非常的快，至少比GNOME，KDE快多了，当然这样比有失公平。



TWM的配置逻辑上被分为三类概念：变量(Variables)、绑定(Bindings)和菜单(Menus)。它们都保存在用户目录下的.twmrc文件中。



变量

变量的配置必须放在第一，它用来描述字体、颜色、指针、边框宽度、图标、窗口的位置摆放，高亮、自动获得焦点等。



变量的名字和关键字是非大小写敏感的。字符串必须用引号引起来，比如：blue，并且字符串是大小写敏感的。



举个例子：



BorderColor gray50{ XTerm red xmh green}

上面表示，所有的窗口的边框颜色为gray50，大致为灰色，括号中间表示特殊的情况，比如第一行的意思是：如果窗口的名字为XTerm，或者它的类名为XTerm(注)，它的边框颜色就为red，即红色的。我们可定义很多窗口元素的颜色，如菜单背景、菜单前景、标题背景、标题前景等。



Color{ MenuBackground  gray50 MenuForeground  blue BorderColor  red { XTerm yellow } TitleForeground  yellow TitleBackground  blue}

绑定

绑定配置通常放在第二位，主要用于描述键盘或者鼠标在窗口、图标、标题、框架上动作时，产生的影响。



比如我们可以把F1键绑定为最小化操作，把F2绑定为更改窗口的层次，把F11绑定为最大化窗口，把Shift+F4绑定为关闭窗口，F12用来把窗口焦点移到某个窗口上。



F1     =        : all    : f.iconifyF2     =        : all    : f.raiselowerF4     = shift : all    : f.deleteF11    =        : all    : f.fullzoomF12    =        : all    : f.warpto XTerm Icon Manager

绑定键盘的语法为：



Button or Key = modlist : context : function

Button or Key，就是鼠标的按键或者是键盘上的某个键。modlist是一些功能键或者它们的组合，比如shift, control, lock, meta, mod1, mod2,mod3, mod4, mod5等，shift, control和lock这些键大家都知道，meta在有些系统上就是alt键。其他的我也没搞明白是什么东西，如果你知道，请告诉我。context表示上下文，所谓上下文，就是指鼠标或者焦点所在的地方。比如上面的 F4键的行，其中的all表示当鼠标指针点在程序的任意位置，shift+F4都会把当前窗口关闭，上下文还包括：



root：  根窗口frame：  窗口的框架title：  窗口的标题window： 窗口的客户区，就是窗口的内部那块区域，学过VC的应该很清楚icon：  图标iconmgr： 窗口管理器all：  就是所有啦

再举个例子：



Button1 = : root : f.menu TwmWindows

表示当鼠标左键在根窗口上点击的时候，弹出TwmWindows菜单，TwmWindows是一个菜单的标志符，我将在后面说明。



上下文可以任意组合，比如想表示鼠标在框架或者标题上的绑定，我们可以这样写 F1 = shift : t|f : f.raise。其中t为title的缩写，f为frame的缩写。其他的上下文也都有缩写。



我们还可以把窗口的标题上加“标题按钮”，比如我们要在标题上加一个关闭按钮，我们可以这样：



LeftTitleButton   /usr/X11R6/include/X11/bitmaps/xm_noenter16 = f.delete

LeftTitleButton表示位置，然后是按钮图标的路径，最后是按钮的动作。



菜单

菜单用于给用户提供自定义单的机会。它们可以被分成不同组，方便管理。每个菜单都由一个名字来标识，这个名字将来用作f.menu的参数。并且，我们还可以定义菜单的背景色、前景色、菜单的项以及该项所对应的动作。如下例：



menu LeftClickMenu{my menu        f.titlefcitx          f.exec exec fcitx &amp;kill fcitx     f.exec exec killall fcitx &amp;  (rgb:0/2/4:rgb:4/b/f)   f.nopXterm          f.exec exec xterm -fn 7x13 -fg gray -bg black &amp;GNOME Term     f.exec gnome-terminal &amp;FireFox        f.exec exec firefox &amp;Luma QQ        f.exec exec ~/bin/LumaQQ/lumaqq &amp;Gaim           f.exec exec gaim &amp;Time           f.exec exec xmessage `date +%F %R:%S [%u]` &amp;}

菜单的内容编辑好后，你需要设置菜单的激活条件。比如上面的菜单，我们让它在鼠标左键点击屏幕时弹出。方法是在.twmrc中加入



Button1 = : root : f.menu LeftClickMenu

Button1表示鼠标左键，root表示根窗口，可以说就是桌面。



正如你所看到的一样，配置非常的简单，其中我设置了一个空菜单，它用来分割不同类别的菜单项，它的颜色和别的稍有不同，括号中的前面表示前景色，后面表是背景色。而最后一项它的动作为f.nop表示没有任何动作。而f.exec表示执行某个程序。f.menu表示激活某个子菜单。



图标管理器

如果桌面上的图标过多，用起来比较麻烦，我们这个时候可以用图标管理器来简化工作。TWM支持多个图标管理器，每个还可以有一列或者多列，比如你想把所有的XTerm类程序的图标都放在一个图标管理器中管理，你可以创建一个如下的管理器：



IconManager{ XTerm  =100x5-10+10 1}

XTerm是窗口的类名(注)，后面的参数表示管理器窗口的位置在屏幕的右上角，大小为100X5， -10+10表示它在屏幕上的位置，最后的1表示它只有1列。这样你所打开的所有XTerm类的程序（比如xterm）的图标都会被这个管理器管理。管理器中的图标缺省是按照窗口打开的顺序来排序的，如果你愿意，你也可以修改排序的方式。



有用的设定

TWM默认情况下，在建立新窗口时，需要用户指定窗口的位置，这个“特色“实在让人头疼，不知道TWM的作者当初的用意何在。还好，有参数可以关闭它，在.twmrc的最上面加入RandomPlacement即可，以后新打开的窗口就会自动的找一个位置了。



在. twmrc中加入AutoRelativeResize，然后你就可以拖动标题栏最右边的按钮来改变窗口大小了。在实际操作中，我发现，如果要缩小窗口，需要先向放大的方向拖动，然后再往缩小的方向拖动才可以。如果不加入这个参数，要想改变窗口大小，需要把鼠标移动到右下角才可以，不够方便。



AutoRaise。有些窗口，我们会经常用到它，比如XTerm类(注)的窗口。为了方便起见，我们在配置中加入



AutoRaise{XTerm}

把你的鼠标移动到XTerm的窗口上，看到了吧，无须任何点击，窗口就会被放到最上层。



结尾

TWM并不是一个完美的窗口管理器，比如它在某种意义上说不够漂亮。但是每个窗口管理器都有它自己独特的地方，每个人都有可能爱上TWM，也许有一天你厌烦了别的管理器，你会尝试用一下TWM，以缓解一下审美疲劳。
