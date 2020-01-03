---
layout: post
title: WP现有中文缩略名批量翻译插件
categories:
- 技术
tags: [wordpress]
status: publish
info: 上海
type: post
published: true
meta: {}
---

前段时间写过[帖子是介绍了可以自动获取标题中的slug信息，或者自动翻译标题信息的插件](http://mooninsky.net/how-to-set-postname-in-offline-editting)。这个当然是很好，但是对于我来说，还有一大批没有设置过英文缩略名的历史文章，这个该怎么处理，我倒是大伤过脑筋。
  
说到为什么一定要英文缩略名呢？主要是看起来不爽。浏览器遇到中文缩略名，就只会处理成一大长串不可读的编码,例如：[http://mooninsky.net/%E6%96%B0%E5%B9%B4%E5%BF%AB%E4%B9%90](http://mooninsky.net/%E6%96%B0%E5%B9%B4%E5%BF%AB%E4%B9%90)——这个其实就是中文‘新年快乐’的编码而已。
  
其次就是有时候这种名字会导致搜索引擎无法正确追踪——至少我在google的管理员工具里就看到这种告警。
  
所以，我下了决心要解决这个问题。
  
事实说明，万事万物都是有解决的，果然看到了这个神奇的插件：[cos_slug_converter](http://www.storyday.com/wp-content/uploads/2008/12/cos_slug_converter.zip)，[关于使用方法](http://www.storyday.com/html/y2007/1219_slug-batch-conversion-plug-in-for-english.html)也很详细的列在了作者的主页上。
  
使用有点特殊，引用如下：

> 废话少说，使用方法，下载这个文件到插件目录，然后后台激活插件。如果你的wordpress没有静态化，请访问 http://youwordpress/?cos=true,否则请访问http://yourwordpress/page/2 /?cos=true,页面将自动现实翻译的状态，一次翻译5个标题，翻译完毕之后请自动往后翻页，直到不能翻页为止，此时则表示翻译结束，有需要的朋友，赶快下载吧。   
>    
> 记住，使用完毕之后让这个插件处于未激活状态，免得带来效率的问题（虽然表面上看几乎没有效率的问题存在）。   

所以我一鼓作气，把以前的历史遗留问题给彻底解决了，终于可以告别那囧囧的乱码标题了。

  
但是，也遇到了一些小问题：
  
1. 由于使用的Google 翻译的服务，那么自然，Google如果翻译的很乱来，那么自然也只能接受这个乱来的结果了；
  
2. 对于标题中含有中文标点的情况，会导致很离奇的翻译：直接把标点也翻译成单词，而且有时候会导致残留部分中文的情况。这个根本原因还是在于1.
  
3. 使用之后，发现页面CSS的h2样式有变，不知道具体原因，必须停用之后，才恢复——当然，这个是无伤大雅的。
  
虽然不够完美，但是依然是非常值得推荐的插件——或者按照作者本人的说法，这个一次性的东西，还是称为工具更好一点。

