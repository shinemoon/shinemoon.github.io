---
layout: post
title: 几个插件配合，Firefox完美书签解决方案
categories:
- 技术
tags: [firefox]
info: 上海
status: publish
type: post
published: true
meta: {}
---

上次说到转投Firefox的阵营了，但是始终还是感觉MX的在线收藏做的比较舒服--最先选用的Google BookMark的add-on还是很不成熟的，刷新速度太慢，而且最致命的是对中文支持太差了。

我理想中的Bookmark，需要有下面两点

第一、和浏览器能够无缝整合，进行自动同步；

第二、备份服务器能够保证稳定可靠，而且是一个开放的Bookmark。

以前的Maxthon其实只是说第一点能够做的很好，然而对于后一点，我觉得就远远谈不上了。

经过仔细的搜查，个人发现这样的组合可以完全达到我的目的：

 Gmarks - 在Firefox当中建立起管理维护Google Bookmark的工具栏，并且可以同步管理Firefox的工具栏，而且无论响应速度和对中文支持都堪称完美；

 Foxmarks Bookmark Synchronizer - 通过专门的服务器来负责Firefox书签的备份和恢复，和以前Maxthon的做法一模一样；

 Box.net Bookmarks Synchronizer - 将本地的firefox收藏夹文件自动备份到Box.net的网络硬盘上去。

我的使用是这样的，我使用Gmarks的同步添加书签来向本地和Google book mark进行添加；使用时则都是用Firefox自身的书签；然后设置Box为每次退出自动上传。

这下可以说是万无一失了--在临时使用的情况下，我只需要在另一台机器上装上其中任何一个插件就可以了，如果万一没有条件使用Firefox，大不了用Google bookmark。

如果至于数据保存，我就不信Foxmarks，box和Google能够一起关门大吉....

PS. 不过回头看看，我这样是不是有点太大题小作了....:)


