---
layout: post
title: Ubuntu下中文输入解决（SCIM in English Locale）
categories:
- 技术 
tags: [linux]
status: publish
info: 上海
type: post
published: true
meta: {}
---

本文是通过阅读学习了以下几篇帖子，试用而来，整理整理而已: 



(1)安装中文支持和输入法SCIM 



(2)英文Locale下使用中文输入法 



(3)ubuntu8.10英文环境下firefox调用中文输入scim



致谢先。





步骤很简单，首先当然是确保正确的安装了中文输入法:



1.首先更要安装中文系统支持。

中文环境的话，就是 系统-系统管理-语言支持

英文环境( System-Administration-Language Support)

当你第一次设置语言支持时，可能会弹出一个对话框，提示你the language support is not installed completely(语言支持没有完全安装),这时候点安装，就可以安装更多的语言支持。

然後，让我们找到列表里的chinese,打上勾，ubuntu会自动帮你下载中文包。

当这些中文包安装好时，确定下面的Default Language是 chinese (china)，然後保存，按 ctrl+alt+backspace注销，重启X-windows(图形界面)，重启後，界面成中文了。

Ubuntu8.04的默认字体是文泉译正黑，感谢文泉译组织对开源字体的贡献！ (1)

2.输入法的安装，我使用的是安装最方便的SCIM，直接可在软件安装管理里找到，如果设置的缺省语言是中文的话，这时应该就可以启用拼音输入了：

输入法安装及设置

如果你成功安装语言支持，重新启动后，按下 Ctrl+空格，SCIM（输入法）被激活了，就可以输入中文了(ubuntu默认安装的是SCIM输入法)。 打开 系统-首选项-scim设置，输入法引擎-全局设置，选择你需要的输入法吧。

建 议先设置一下输入法，因为是默认的scim输入法可能会与realplay、acrobat reader、openoffice等程序有冲突，所以使用scim-bridge替换scim。安装scim-bridge 和scim-qtimm。请确保已正确设置中文环境，打开终端，执行以下命令，或使用《新立得软件管理器》，在其中搜索”scim-bridge”、 “scim-qtimm”并标记安装。

在终端输入

复制内容到剪贴板

代码:

sudo im-switch -s scim -z default

sudo apt-get install scim-qtimm

sudo apt-get install scim scim-pinyin scim-tables-zh im-switch scim-qtimm scim-bridge scim-bridge-client-gtk scim-bridge-client-qt scim-bridge-agent

编辑im-switch生成的scim配置文件

复制内容到剪贴板

代码:

gksu gedit /etc/X11/xinit/xinput.d/scim

将默认的 GTK_IM_MODULE=scim 修改为 GTK_IM_MODULE=”scim-bridge”。

另外，在scim输入法中进行了如下设定：

scim设置－全局设置－将预编辑字符串嵌入到客户端中 前的勾去掉

scim设置-gtk-嵌入式候选词标的勾去掉

事实上SCIM输入法还是会与一些程序有冲突的，所以在某些软件在安装后要配置文件。

如果大家想使用其他输入法可以 fcitx输入法安装及设置（Kubuntu下推荐使用）（1）

3.但是很多时候，其实有人（比如我）确实不想用中文作为系统缺省——因为字体显示啊，菜单排列啊，都有点不习惯，特别是所谓的中文版都不可能是完全的中文化，所以宁可继续用英文的系统语言，所以这种找抽的行为就意味着额外的劳动：



如果你在英文locale下，正确安装scim或fcitx后仍无法正常使用输入法，解决的方法如下，用im-switch来切换输入法设置：

sudo aptitude install im-switch



如果你用scim，运行



sudo im-switch -s scim -z all_ALL

im-switch -s scim -z all_ALL (2)

而如果不想安装im-switch的话，也可以手动修改：

编辑 /etc/gtk-2.0/gtk.immodules(如果存在的话) 或者 /usr/lib/gtk-2.0/2.10.0/immodule-files.d/libgtk2.0-0.immodules 文件，在xim 的 local 增加 en 也就是说：



"xim" "X Input Method" "gtk20" "/usr/share/locale" "ko:ja:th:zh"



改成



"xim" "X Input Method" "gtk20" "/usr/share/locale" "en:ko:ja:th:zh"



保存退出，重启后再进就ok了.(2)

4.即使现在英文的系统也可以使用中文输入了，但是在某些程序，比如Firefox当中，仍然可能有问题（或者按照帖子的说法，是必然有问题）：

在这里/etc/X11/xinit/xinput.d/

举例来说

如果我们的系统环境是英文，那么我就就修改all_ALL或者default文件all_ALL是default的软链接。

如果是系统为中文环境，输入法有问题，那就要改zh_CN了，以此类推，明白？

在修改之前，先看看为什么中文环境下firefox输入中文没问题？

打开zh_CN

看到这些关键字

GTK_IM_MODULE=scim-bridge

QT_IM_MODULE=scim-bridge

在打开default看看

什么？ 空的，没写？难怪输入不了中文，

GTK_IM_MODULE=

QT_IM_MODULE=



我们把它补上

GTK_IM_MODULE=scim-bridge

QT_IM_MODULE=scim-bridge



在log out，重新登陆英文环境试试，firefox应该可以输入中文了。（3）

5.最后还是要记得把SCIM放到自动加载的session当中，免得每次要手动来切换：

另外Ubuntu 8.10中 ， scim不能自动加载，总不能每次登陆都让我用命名行输入scim吧，烦死了

在这里把它加入到登陆要加载的应用程序中去

System-Preferences-Sessions-startup programmes

add一个，名字叫scim, command为 scim

这样就可以每次登陆自动加载scim了，弥补了系统的不足。

至此，已经可以很好的在英文系统中使用SCIM进行中文输入了。



补充，有朋友提到了新的问题，虽然我没有遇到，但是列在这里以备有类似情况的人参考。

我第一次按着你的方法做没有成功，但是加上了http://www.bitscn.com/linux/system_manage/200804/139603.html说的方法，终于让scim里的中文输入出现了－－原来是scim出现但左键点它的图标什么都不出来。




