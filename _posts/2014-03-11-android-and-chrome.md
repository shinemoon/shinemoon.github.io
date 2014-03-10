---
layout: post
title: Android & Chrome
published: true
tags: [ Chrome, Android]
categories: [技术]
---

> The King is Dead, Long Live the King! 

我指的就是Android和Chrome——姑且神棍一把：在不久的将来，我们可以很清楚的看到Android这个过渡系统的式微（或者更可能一点，是被逐渐逐渐的淡化合并）并且让位于Chrome-Based的新系统，如果要给个期限，1.5个大版本之内（如果不是更早的话）吧。毕竟像Google这样把技术演进和公司战略统一得如此严丝密缝，兼且配上一步一个脚印的坚实执行力，简直是到了让人觉得可怕的程度，实在无法揣测他们的步伐到底会多快。

当年看见类似「操作系统的未来在Web技术，Android只是在这超前理念可以变现之前的一个过渡」这种论调时，我还一厢情愿认为这只不过是买下Android之后，Google的遮羞之词罢了。可是，越来越多的事实让我不得不相信，Google真是这么想的，而且，确实也是这么一步步将前景开始变成了现实。

移动系统上或许端倪还不那么明显，但是不妨先看看Google在桌面系统上的动作:

从最初的chrome extension到后来更强调app，然后，开始大力推广packaged app，并且逐步收紧各种安全限制，并且各种强调packaged app、离线app，仿佛是自废武功一样的把原本相对自由的web应用加上了诸多的条条框框，沙盒以及消息机制虽然安全，但是老让人有点束手束脚——特别是废掉了eval机制，把好端端的js脚本语言整得格外复杂；

这些都让我不解过，直到Google推出了ChomeOS，并且力推ChromeBook，我才算是大概理解了他们的思路。原来他们玩真的啊，想构造一个基于web前端技术的桌面平台；但就算那个时候，我都还是保持着观望和不屑的态度：就凭那些简陋的网页打包就想替换掉桌面系统？也没少看到那些媒体评测对ChromeBook的冷嘲热讽。

然后，我就被去年圣诞商战美国笔记本市场的ChromeBook的亮眼成绩打脸了。在这之前，Native Client的技术的支持和推广其实已经吹响了Google开始动真格的号角——

接着，Google真动手了，Chrome App for Desktop成为了去年年底至今的重头戏；如果放着半年时间不去关注这块，然后忽然去体验一下，真是会被Google的快速演进所震惊。

如下三张图，第一张就是我当年鄙视的所谓的单独app——说到底，就是一个弹出的网页罢了，看着那浏览器的框架死板的框住内容，实在是让人提不起精神；

![feedly](http://i340.photobucket.com/albums/o350/claudxiao/browserbased_zps58d2b7fc.png)

接下来，就是真正的packaged app——选择了No Browser Frame的窗口模式，简单讲，你可以真正的定义属于的你App窗口的每一个像素——用你喜欢的任何web 前端技术。还有比这更爽的UI设计过程么？

![Mado](http://i340.photobucket.com/albums/o350/claudxiao/Mado_zpsbc86e7e1.png)

![Paladin](http://i340.photobucket.com/albums/o350/claudxiao/paladin_zpsf86a2f84.png)

而且一些画龙点睛的细节，也确实标志着Google的野心：

App Launch 开始方便的驻扎进了Windows的快捷访问栏，OSX的Dock；APP的图标独立，并且可以方便的Pin在任务栏或者Dock——而且，Google和以前不同，如果你没有打开Chrome，而是直接使用Launch选择packaged app，那么除了单独打开的app之外，用户根本看不到任何Chrome在后台运行的迹象（当然，打开任务管理器或者是top之类，依然无所遁形）；

![launcher](http://i340.photobucket.com/albums/o350/claudxiao/5C4F5E555FEB71672014-03-11123531AM_zpsfefaf4e2.png)

此外，这样的「小细节」加上刚才提到的app窗口本身目前几乎是完全的独立，Google基本上已经抹平了所谓的Chrome APP和传统的Native程序在UI之间的区别，至少普通用户是无法分辨的；

同时，是为了「逼真」吗？Packaged APP的页面中，无法实现href的跳转、无法审查元素（除非打开flag中的调试）、当然也不可能让你刷新——的确扑朔迷离无法分辨。

至于常被人说起的诸如安全性、开发复杂度（特别是一些算法等等）的问题，我能看到想到的，也就是NACL了，简单、直接、但是的确好用，不管怎样，C/C++始终不会孤单——再配合上Google逐步加强的，设备相关的API的深化（特别是考虑到日渐增多的ChromeBook和依然由Google把持着的Android），手机和其他移动设备厂商间的「军备竞赛」等等因素，Chrome App注定可以用Native App的姿态出现在更广泛的设备上的——更重要的是，其实Chrome从最开始想做的，就不是一个简单的浏览器，而是一个操作系统，甚至是一个可以锲入到对手OS中，不动声色构建属于自己的生态的平台。

而回到Android上来，Google有能力，并且早就开始做到对Linux的深度Chrome化定制，如果放到本来就由它主导的Android身上，恐怕更加轻松，虽然目前的进展和桌面端比起来偏保守，还停留在桌面加APP入口、打开后全屏的[初级阶段](https://developers.google.com/chrome/mobile/docs/installtohomescreen)，可是Google有一直负责Chrome的皮采来兼管Android，又何愁进展？目前移动设备越来越逆天的配置更是让可能出现的对性能的担忧日益减轻。

用不了多久，花不了几个小版本的更迭，Chrome就会成为Android中更加底层和重要的平台， Chrome App on Android恐怕就会慢慢成为Android上的主流——到了那时候，成功完成了智能手机早期攻城拔寨任务的Android也就离功成身退不远了，而Google 这一盘棋才算是开始收线了。


