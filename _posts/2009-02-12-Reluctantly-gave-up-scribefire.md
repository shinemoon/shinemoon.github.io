---
layout: post
title: 忍痛放弃了ScribeFire
categories:
- 技术
tags: [firefox]
info: 上海
status: publish
type: post
published: true
meta: {}
---
这两天一直在忙着捣鼓域名绑定的事情，遇到一切的问题，第一反应都以为是这方面导致的情况——于是也很是骚扰了Oneoo几次，拜他的迅速反应和负责，还是相当顺利的摆平了这一切，直到我发现自己的ScribeFire没有办法连接上的Yo2的时候。

刚开始当然觉得这是小问题，或许只要把设置里的地址修改修改就可以了——结果不行；

接下来我就试着删掉重新来创建账户，结果依然不行，直接卡死在链接的步骤上了；

然后，叹了口气，心想趁这个机会，把这个偶尔会不稳定的ScribeFire换成我心仪已久的Zoundry Raven吧？结果，一样的惨，Zoundry可以成功的发文（但是，如同很多人反映的，没有办法顺利的得到发文成功的回馈），不过却始终刷不出blog list来，让我看着Zoundry那华丽溜溜的功能兴叹；

我想了想，直接在Google Talk上ping Oneoo，心想这下总没问题吧：他依然很热情，也很迅速，测出了在Windows Live Writer上是没有问题的，我大惊，连忙打开LiveWriter，果然啊。

实在不好意思再继续骚扰Oneoo了，唱了个诺，灰溜溜的开始专心用Windows Live Writer了。后来才发现，其实这个和我是不是绑定域名没有任何关系，因为我有另外的未绑定的帐号，以前一切正常，现在照样不能用了——灵异啊。不管那么多，反正Live Writer也有，我就坚持用这个号称‘微软唯一的不被骂的工具’来发布YO2文章吧——正如我一向用‘腾讯唯一不脑残的服务’qq邮箱来发布QQ空间+Live Space日记一样。

其实Live Space的确是很好的工具，唯一的不方便也就是和ScribeFire比起来，不算是个lite tool，偏大了一些，但是功能上，应该说其实更加强大了，更何况——我现在有的选择么？可爱的ScribeFire啊，我只能先放弃你了，可惜了3.2版本里刚改换的漂亮的icon啊。

问题的解决方法（2.25更新）  ps. 今天读到了

[ScribeFire无法连接yo2的原因及解决方法！](http://p3p3pp3.yo2.cn/archives/43142) 

对比两个软件的http request，并逐项修改尝试，发现原因竟然是yo2的博客对firefox的Useragent有歧视：    

ScribeFire的请求中UserAgent为：User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.6) Gecko/2009011913 Firefox/3.0.6 (.NET CLR 3.5.30729)

WLW的请求中UserAgent为：User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Windows Live Writer 1.0)

在RequestBuilder中修改ScribeFire的UserAgent并Execute，发现返回的数据正确！！

遂在Firefox中安装User Agent Switcher扩展，切换一个其他的UserAgent，发现ScribeFire顺利的注册上博客帐号，使用正常，本文就是使用ScribeFire最新版本3.2.2发布。

依样画葫芦，果然得以解决。不意，到了今天忽然又不习惯ScribeFire来写博客了，觉得更顺手的还是WLW... ...习惯真是太可怕了。

