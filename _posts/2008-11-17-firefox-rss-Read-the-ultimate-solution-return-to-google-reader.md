---
layout: post
title: 'firefox RSS阅读的终极解决——回归Google Reader'
categories:
- 闲话
tags: []
status: publish
info: 上海
comment:  年轻的时候偶尔和老美开个会还真没当回事……现在神烦
type: post
published: true
meta: {}
---
今天晚上为了开一个比较晚的，试图和美国，以色列等多方撕扯的讨论会 ，加上Laptop的系统忽然做欲崩溃状，害得我长途奔袭外加紧张兮兮——不管怎么讲，总算是没出什么毛病。结果虽然很困，现在却睡不着了。

以上是碎碎念的废话，以下是正文。

很早就开始使用在线的RSS阅读器了，应该说这是趋势。在所谓信息爆炸的年代，脱离了RSS阅读，那么要么就是摄入信息不足，要么就是被彻底淹没；而在线的阅读器，较之离线，同样优势明显。

Google Reader曾经就是我最早的选择，但是用了一段时间之后，但是感觉服务器不够稳定——此外，顶部那功能树也让我不太习惯。

接下来是鲜果，这个如今算是炙手可热的国内产品，的确不错，UI上给用户感觉友好许多，但是，一些莫名其妙的seed丢失现象让人防不胜防，大倒胃口，只好又去使用抓虾。

抓虾算是我用的很长的阅读器了，可是，用着用着，发现自己终于不能忍受它抽风似的无法刷开文章列表这个痼疾了。

而且，对于我这个轻度firefox中毒者来说，鲜果、抓虾和firefox的结合度实在不如GR。

于是我再次看向了Google Reader。

这次才确认了这早就该确认的道理：在Firefox上，只要勤劳好学，一切都好解决。

打开我的Google Reader，导入了我从抓虾里面导出的OPML文件，一键搞定，稍微稍微整理一下目录就可以上路了，再把阅读的页面设成缺省主页——到此Google Reader的任务就算完成了。

接下来解决两个问题：

1. 我不喜欢的界面问题： 求助万能的[stylish](https://addons.mozilla.org/en-US/firefox/addon/2108)吧,这个借助用户CSS可以进行基于站点的页面定制的插件，拥有许许多多的用户脚本，自然少不了Google Reader的份，随便搜搜吧，很容易就找到了[Google Reader - just tree and chrome](http://userstyles.org/styles/4519) ，如同自述所言，这就是精简GR页面，只留下阅读框架的脚本。

看看对比图，就很直观的知道了：

Before

![pic](http://userstyles.org/style_screenshots/4519_before.png)

After

![pic](http://userstyles.org/style_screenshots/4519_after.png)

需要做setting的时候，只要临时在stylish里disable这个脚本就可以看到GR的顶部内容了。

当然，各有各的喜好，完全可以自己搜搜，找个自己喜欢的样式，比如MAC之类的。

2. 定时自动检查提醒的功能：这个就更好说了，[Google Reader Watcher](https://addons.mozilla.org/en-US/firefox/addon/4808) 算是蛮老牌了，方便，快捷，就只是占据了状态栏一个小小的角落罢了。看见更新了，鼠标过去悬停看看，觉得攒的够多了，双击一下图标进入GR看新闻——这是件惬意的事情。

![pic](https://addons.mozilla.org/en-US/firefox/images/p/13561/1177153144)

![pic](http://i340.photobucket.com/albums/o350/claudxiao/short.png)

PS. 有点小提醒，Google Reader 在Firefox3下好像偶尔会出现阅读界面始终刷不出的问题（此时上部的登录界面却可以刷出来），遇到这种情况，是Firefox的隐私内容出了点小问 题，只需要清一下，ctrl+shift+del, OK, 至少我是可以解决的。

总结下，GR的阅读体验不错，快捷键也方便，更重要的是，我看好它，毕竟现在各大手机商对Google的支持是没话说的，何况眼看着Android系统也要风生水起，跟着GR混，用一个能够在任何地方，任何设备接入同一个RSS阅读服务，这样的诱惑力是很难抵御的啊。

夜了，晚安。


