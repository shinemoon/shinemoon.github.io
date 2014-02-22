---
layout: post
title: 从Wordpress到Jekyll
categories:
- 技术
tags:
- wordpress
- jekyll
status: publish
type: post
published: true
info: 杭州
meta:
---

在Host2ez上托管基于Wordpress的独立博客已经两三年了，一直也算是满足于相对便宜的空间价格和还算不错的服务；但是仅仅是一个简单的wordpress的服务（而且本人博客也远远够不上红火），却在近期遇到过两次所谓流量超限的情况，实在有点让人哭笑不得，于是动了再次折腾的念头。

这次，稍加思考，就决定了Jekyll这个静态博客的方案。

写了这么久的blog，现在早就已经算是「反璞归真」，心无杂念了，但求有一个可以干干净净写字，踏踏实实保存的地方就可以了——免费空间尤佳。

基于Jekyll的Github Pages无疑是能够完全满足上述要求的服务。

具体的建站方法，只要稍加搜索就不难找到，特别是Github Page自身的页面说明也已经[足够清楚](http://pages.github.com)，我想说的是在这之外的一些「水面下的工作」。

首先，从wordpress导出的xml文件导入到Jekyll的系统的任务，在Jekyll的网站上可以找到说明。准确的讲，就是一条现成的Jekyll import的命令就完成了，简单，清爽——可是，这也就意味着，如果你想导入历史数据，那么，按照Github的建议，[在本地搭建一个Jekyll的环境](https://help.github.com/articles/using-jekyll-with-pages)，几乎就是一个必须做的事情了，而这其中涉及到的从Ruby环境安装配置，到因为GFW导致的GEM工具访问源的不稳定（从而需要用国内镜像来规避），都是不动手做都不会想到的问题，所以，千万不要心怀侥幸。

接下来，当我导入完成之后，发现两个严峻的问题。那就是由于多年来混迹各个BSP之间，导致的关于文章标题和内容格式的极度混乱的状态，让整个_posts目录简直没法看。

特别是为了能够平滑保留多说系统的评论内容，我想用无后缀名的页面地址，可是由于早年不讲究所导致的中文文章标题，在这种情况下似乎有bug，无法正确生成链接。更不用说以前的那些中文标题名体现在文件名上，都是眼花缭乱的URL编码；

所以我决定开始把所有这些乱码文件名都改成英文的……改了十几个之后，我就退缩了。开始写python，先URIdecode变成中文，再用google translate变成英文，最后重命名，幸亏有这种好工具，[好歹花半个晚上脚本](https://github.com/shinemoon/shinemoon.github.io/blob/master/_posts/filename_change.py)，再花了点时间转换，可算是搞定了。

其次是早就知道的问题了，导出的生成的文件都是html格式，基本上内容都是各种tag满天飞，而且05年以前的博文，直接格式在我上次搬移的时候就已经丢失了，不管多长的文字都是一行到底，到了这个时候才深切的感到markdown的美，面对这十年间写下的550多篇文章，就算垃圾，也忍不住想好好整理一遍，所以我就开始逐篇进行格式转换甚至是添加「注释」了。然后，几乎导致了这段时间的睡眠严重不足甚至是肩周疾病……

然后发现想做Categories和Tags需要自己稍微写下plugin才行，于是我就吭哧吭哧学着写了两个，好不容易本地实现了，挺高兴了——发现Github是直接打开safe开关，禁止插件的。

所以只好写两句shell，每次都本地build好了再上传。

最后，为了能够满足强迫症患者的心理，除了我常用两台电脑上本来就有这个repository之外，又用网盘同步了一下_posts目录，这样理论上的风险已经降到了很小的程度因为抬头想想，就这么几篇破文章，实际上保存的地方有：我的MacAir，我的公司的Windows的Laptop，Github，坚果云，哦，还要算上我的Time Machine……

至于主题设计什么的，我是一切从简——唯独友链不能丢，虽然现在活着的友链也没几个了。

一直到了今天，才终于算是重体力劳动的部分告一段落，有时间来写下这个消息，[并且开始正式准备切换DNS到Github了](https://help.github.com/articles/setting-up-a-custom-domain-with-pages)，希望切换顺利。

我这是越忙越折腾的作死的节奏啊。


