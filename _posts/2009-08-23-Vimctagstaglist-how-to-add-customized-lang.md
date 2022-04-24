---
layout: post
title: 如何在Vim+Ctags+Taglist应用中添加自定义语言
categories:
- 技术
tags: []
status: publish
info: 杭州
type: post
published: true
meta: {}
---

Vim+Ctags+Taglist的应用是一个非常方便的解决方案，网络上关于这样的简单介绍数不胜数，只要愿意不妨搜索一下即可。但是有一个问题是大多数文章没有阐明的，那就是如何添加原本不被Ctags和taglist所支持的语言呢？花了点时间，找到了解决，姑且备忘于下，希望利人利己。本文均以SystemVerilog为例说明：

###Ctags中添加新的语言###

ctags的配置文件其实在 ~/.ctags中，打开该文件，添加如下代码

1. 从某论坛上看到，做了一定修改，用以支持extern,static等前缀：

<pre>
--langdef=systemverilog
--langmap=systemverilog:.sv.svh.svi
--regex-systemverilog=/^[ 	]*(virtual)?[ 	]*class[ 	]*([a-zA-Z_0-9]+)/2/c,class/
--regex-systemverilog=/^[ 	]*(extern)?[ 	]*(static)?[ 	]*(virtual)?[ 	]*task[ 	]*.*[ 	]+([a-zA-Z_0-9]*::)?([a-zA-Z_0-9]+)[ 	]*[(;]/5/t,task/
--regex-systemverilog=/^[ 	]*(extern)?[ 	]*(static)?[ 	]*(virtual)?[ 	]*function[ 	]*.*[ 	]+([a-zA-Z_0-9]*::)?([a-zA-Z_0-9]+)[ 	]*[(;]/5/f,function/
--regex-systemverilog=/^[ 	]*module[ 	]*([a-zA-Z_0-9]+)/1/m,module/
--regex-systemverilog=/^[ 	]*program[ 	]*([a-zA-Z_0-9]+)/1/p,program/
--regex-systemverilog=/^[ 	]*interface[ 	]*([a-zA-Z_0-9]+)/1/i,interface/
--regex-systemverilog=/^[ 	]*package[ 	]*([a-zA-Z_0-9]+)/1/k,package/
--regex-systemverilog=/^[ 	]*typedef[ 	]+.*[ 	]+([a-zA-Z_0-9]+)[ 	]*;/1/e,typedef/
--systemverilog-kinds=+ctfmpie
</pre>

这里从代码可以读出无非是依次定义了新的语言种类，指明了文件后缀，然后使用正则匹配来抓出你希望的关键字，熟悉正则表达式的人自然一读就懂，可以自己扩展，不熟悉的人，那就照copy吧。

###Taglist中添加语言种类###

打开taglist的文件，例如 ~/.vim/plugin/taglist.vim, 添加下面的内容：

> systemverilog languagelet s:tlist_def_systemverilog_settings= 'systemverilog;m:module;c:class;' .


>t:task;p:program;f:function;i:interface;e:typedef
   
语句也很简单，就是添加了一类可以被Taglist识别的语法种类，同时规定了那些部分是需要显示在tag list当中的；

###Vim当中添加File type###

似乎有点本末倒置了，呵呵，其实最开始的一点就是要让vim也能够识别出systemverilog的文件，那么请打开~/.vim/filetype.vim，加入下面这一行：

> au BufNewFile,BufRead *.sv,*.svh
> setf systemverilog
 
 
同时不要忘记'set filetype on'来保证vim会去识别语法种类（当然，这个其实也是使用语法高亮的基本要求）。

###步骤###

使用的时候，无非就是按照：

1. ctags -R * 来生成tag文件；

2. vim打开文件，并且可以适当设置' set tags=xxxxxx' 来load文件；

3. 用:Tlist打开tag侧边栏，其余都可以按照网上教程操作。
