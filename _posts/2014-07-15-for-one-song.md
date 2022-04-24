---
title: 为了顺手存一首歌
categories: 技术
tags: [chrome]
type: post
info: 完工后
comment: 折腾，但是算是最贴合自己需求的扩展了。
published: true
layout: post
---

故事的起因大概是这样的，某天下午，八百年不怎么听歌的我顺便听了听就没打开的虾米，无意中听到了一首歌，于是，回忆起了好多年前还在用Firefox的时代，曾经用过的流媒体下载扩展；

再进一步回忆一下，想起了自己刚从Firefox转向Chrome之后，也花了好大的功夫想寻找下类似的插件结果未遂的经历；就连开始玩票性质写点扩展之后，还试图考察下为什么没看到Chrome上有类似的工具，结论是，当时的Chrome并不支持对network的stream的监控的API，就算有，好像那时还放在Experiment类别里，于是怏怏作罢。

可是，时过境迁，再次挖掘这个老坑就发现了的确今非昔比，从v18开始，好像Chrome就支持了对WebRequest的监听和操作；那还有什么好说的，自己动手丰衣足食呗；

所以开始埋头苦干写起了扩展，花了大概三个晚上的时间完成了大概的虾米音乐的监控、下载管理等，接着又想起，难得开头写了，最近几个百度网盘转Aria2的脚本好像都失效不怎么好用了，要不，顺手也写了吧；

至于Aria-jsonrpc什么的，虽然小众，但是用过的人，当然能理解这个神器的妙处所在了，为它花点功夫（大概一个晚上左右），还是值得的。而且基于[前人的工作][1]，开发也是相当的简单。

不管是虾米还是百度Aria的支持，「关键技术」本身都是很简单的，无非一个WebRequest的监听，和对aria jsonrpc的直接使用；真正花功夫的还是一些蛋疼的细节罢了，例如，在网页上图标的插入和Ajax刷新之后的动态监测、chrome的下载bar的显示隐藏时机、页码的跳转显示等等。

总而言之，[终于完工，这次懒得写什么说明，精修截图之类的了，糊弄着上传store][2]，纯粹自用，然后很满意的，试图回想起大概一周前，那首让我起了念头的歌到底是那一首？

![enter image description here][3]

结果，我忘记了。


  [1]: https://github.com/ghostry/toAria2
  [2]: https://chrome.google.com/webstore/detail/%E4%B8%8B%E8%BD%BD%E5%B7%A5%E5%85%B7%E9%9B%86/bbkbmckcblbohnkkhjknhggkjloiklio
  [3]: http://i340.photobucket.com/albums/o350/claudxiao/Untitled_zps6176f66e.png