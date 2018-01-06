---
layout: post
title: 怎样利用离线工具同步发布Wordpress与Qzone
categories:
- 技术
tags: []
status: publish
type: post
info: 杭州
published: true
meta: {}
---
想要同步发布Qzone固然是个恶俗的需求，但是也的确是个有意义的要求，否则也不会有牛人专门的[post-to-qzone](http://liguangming.com/view/783)的插件来完成这样的功能（也包括对Windows live Space的同步发布）；

不过Post2QZone的缺陷也很明显，它要求用户是在Wordpress的管理后台来发布文章，这才可以实现同步发送的目的，而这对于从来不用wordpress后台直接发文的我来说就是一个有些鸡肋的功能。于是后来我也放弃了这个插件。

反而是无意之中看到一位[Z-blog的兄弟的解决方案](http://www.xiaoxiaozhu.cn/post/mail-blogger-livespace-qzone.html)，让我受到启发，Z-blog可以，没道理Wordpress不行，于是经过尝试，发现的确是一个很好解决的问题。

不过稍微有那么几个步骤要做，分别是从：


###QQ邮箱###

因为同步的基本原理依然是逃不开用qq邮箱来邮件发布qzone文章（这也是腾讯官方为qzone打开的唯一的外部接口），所以要从qq邮箱着手。

首先是要把QQ邮箱的SMTP使能，请到qq邮箱的设置-账户当中，找到POP3/IMAP/SMTP服务的内容，然后勾选开启IMAP/SMTP服务的选项。

当然，如果以前没有用邮件发布过qzone的话，建议先看看这篇官方指导，[如何通过发送邮件的方式发表Qzone](http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=23&&no=242),简单说来就是向您的QQ号@qzone.qq.com这个邮箱地址发送邮件就ok了，前提是它只会接受和识别从你本人的qq邮箱发出的邮件。

###Wordpress后台###

通过上面一步不难了解，我们要做的事情其实就是两件：

让Wordpress可以用QQ邮箱发信，以及有新文章的时候可以自动对特定的邮箱地址发送新文章；

知道了这个之后，我们下面就是找到对应的插件了，很幸运，的确有现成的好东西：

对于前者，我们可以使用WP-Mail-SMTP来设置wordpress所有的邮件都从指定的SMTP服务器发送，题外话，这个方法也可以解决那些不愿意看到留言提醒的发件人总是[wordpress@xxx.xxx](mailto:wordpress@xxx.xxx)的不爽——当然，如果看到的是qq.com之类的愿不愿意，这个，算是一个小小的缺憾吧。

关于WP-Mail-SMTP的介绍，网上内容很多，不妨自行查找，需要补充的就是安装之后，需要到WP后台的设置-EMAIL当中修改一些内容：
选择好From Email，填入自己的qq邮箱地址；

将Mailer修改为&#039;Send all Wordpress emails via SMTP&#039;;

将SMTP Options中的SMTP Host填为qq：  smtp.qq.com

建议不使用SSL加密,因为我使用之后神秘失败……

最后填入用户名和密码。

Update之后，建议试试发送一封Test Mail，反正很方便；
接下来就是解决有文章更新自动发送邮件的问题了，那就要靠Post Notification了。

它的作用原本是用来实现邮件订阅的，每次有新文章，可以实现自动给订阅者邮箱发信。应该说这是个很强大的插件，可以自定义发送的格式，附带的信息，甚至顺便也解决了你到底是愿意全文发送还是发送摘要。

那么安装之后，到设置-Post Notification当中，进行如下的配置：
首先， Manage addresses，记得将自己的您的QQ号@qzone.qq.com添加到订阅列表，这里也可以选择你愿意将哪一类分类的文章发送到Qzone；

接着到setting当中，修改几个关键参数：

Look当中，是否需要发送全文，Copy complete post in to the mail，可以灵活选择全文，摘要，还是到more标签；

Profile是选择使用哪个语种的配置，建议用en_US，这个决定了等下去修改模板文件是在哪个目录下；

Template是决定使用哪个模板，缺省有纯文本的txt和html的格式，当然用html，否则图片就没办法显示了；

Subject是标题格式，缺省是用博客名称+标题；

后面的关于发送邮箱建议用自己的qq邮箱以防万一（本人没测试过别的填法）；

其余的一些设置，可以使用缺省。

最后，到Test里，试着发送一下，不过这里的对象邮箱必须是你已经添加到订阅列表的邮箱，至于Post id，如果你发现自己没法在文章-编辑中看到，那么请安装Restore Post Id这个插件来恢复id栏。
到此为止，基本上已经可以，不过有追求的人，通常对邮件格式也会有点不爽，因为里面会带上一大堆诸如“此邮件是xxxx发送，因为你订阅了xxxx，请访问xxxx来如何如何”的废话，想修改这个，那么就要修改模板了。

###模板修改，Cpanel或者Ftp###

进入自己的blog的Cpanel面板或者直接ftp登录，找到Post notification的安装目录（这个插件安装的目录，我想属于基本知识，可以自行学习），然后在下面的en_US的目录里你就会发现设置里提到的几个模板email_template.html, email_template.txt等。

用你喜欢的方式打开，修改，替换——主要是把那些“过分礼貌”的文本给去掉。

当然，有美感追求的人，可以自己去做进一步的修改。

但是一件非常让人无奈的事情就是，qq邮箱发信到qzone的过程当中一些标签会被丢失，其中甚至包括h1，h2等常用的内容，更不用说还有blockquote之类的东西了，实在是无语。关于这一点，官方的回答是，可能是由于qzone日志编辑器更新，但是邮箱发布功能未能更新导致的bug，会尽快解决，那么就静观其变吧。

因此不妨留意，对于想发布到Qzone的内容，格式上还是朴实一点的好……

###结语###

综上，不论如何，总算是把Qzone的同步给搞定了，而且这个是脱离开具体发布方式的，不论是直接后台发布还是任何一种离线工具，都可以自动的把文章发送到Qzone。所以应该说这是一个普适的方法。

这个纠结了我很久的问题，在我昨天晚上心血来潮的30分钟以内就搞定，必须说，我颇感唏嘘，解决这个并非目的，有意思的其实是解决的过程，引用一句话作为结语：

Engineer is nothing more than a problem solver.

2009-10-14补记:  [post-to-qzone-v0.4](http://liguangming.com/view/783)版本解决了离线博客工具同步发布的问题，这样相信可以省下不少的力气，有兴趣的朋友不妨直接使用。
