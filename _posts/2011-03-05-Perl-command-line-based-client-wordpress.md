---
layout: post
title: 基于Perl的命令行Wordpress客户端
categories:
- 技术
tags: [wordpress]
status: publish
info: 杭州
type: post
published: true
meta: {}
---

在使用过许多离线的博客编辑器之后，我发现自己对于编辑器的要求越来越极端了，轻巧，快捷，编辑器本身的舒服——同时对于多媒体类型的编辑功能的要求却非常的低；无疑，从Windows Live Writer到FireScribe，包括多平台上的各类开源闭源，收费免费的种种工具，大家多半走的是大而全的路线，所以到了最后，我打算自己干脆折腾一个算了。


加上在Ubuntu上试过Pyroom以后，这种Distraction Free的编辑器给我感觉非常的舒服，更是发生了：如果能用这个直接写博客该多好啊？这类奇怪的想法，不过看了看XMLRPC相关的资料以后，我发现这个想法一点都不奢侈，简单的Perl脚本就完全可以搞定了，不如自己动手DIY吧。


我希望实现的目标如下：




- 创建新的博客文章；


- 删除新的博客文章；


- 有限的编辑最近文章，对我来讲5篇就足够了；


- 无论新建还是编辑，对于该篇文章的各个参数要能充分设置；


- 可以配合自己喜欢的编辑器；


- 支持代理服务器；


- 可以本地保存草稿；






鉴于我既然坚定的需要基于简单的文本编辑器来完成这样的动作，那么做出的平衡自然就是如果用这样的方法，我显然只有老老实实的写HTML代码了——比起所见所得的富文本编辑器当然是要麻烦一点，但是习惯以后，却也自然有它的方便之处。

编写过程意外的顺利，无非是些Perl基本东西，唯一让我稍微头疼了一下的问题，是中文字符在做HTTP Request时会遇到Message must be bytes的错误，经过一番查询，发现必须在做content之前做一个utf8的encode动作，不得已，只好把Frontier::RPC2的包复制到本目录下，改个名字，加入了这个encode的预处理才算是搞定，不过这样一来，倒也省去了要用户先行安装Frontier包的麻烦，只要编辑一下脚本里的路径就好了。



老习惯，代码依然托管在Bitbucket，链接如下：





[perlWP 项目链接](https://bitbucket.org/claudxiao/perlwp/wiki/Home)
[perlWP 下载链接](https://bitbucket.org/claudxiao/perlwp/downloads/perlWP.tar.gz)



直接在本地建立一个目录，将所有文件复制到目录下即可，重点在于修改perlwp的配置内容：

当然，你也可以在任意地方建立你希望的lnk来指向它，例如放置在常规放置bin的位置。


#######################################################
#Default setting
#Please Modify Below Configurations If Needed
#######################################################
use lib '\[dir\]'; #路径请使用绝对路径，例如/home/username/xx/,而不要是~
my $url  = "http://yoursite.site/xmlrpc.php";
my $user ="xxxxxxxxx";
my $pwd="xxxxxxxxxxxxx";
my $editor="vim";
my $proxy = "proxy";
#######################################################


使用命令和简单，用perlwp -help就可以看到详细的帮助，顺便也贴在下面：




###NAME###

perlwp - Use Perl command line to post/edit/manage your wordpress blog.


###SYNOPSIS###

	perlwp \[OPTION\]


###DESCRIPTION###

perlwp is a simple perl script to post/edit/manage your wordpress blog via xmlrpcl.php. Only commandline is needed as the interface, and user can use any favorite editor to edit the pure html post content, while most post parameters including title, slug, tags, categories and so on can be defined easily.
\-user=sthe user name for your blog, if ignored, default user name in perlwp file will be used;
\-pwd=s		Set the user password for your blog, if ignored, default user password in perlwp file will be used;
\-editor=s	Set editor,if ignored, default editor in perlwp file will be used;
\-c		Create new post/Open existed draft to continue, depends on if any existed draft there;
\-e=s		Edit the post with postid equal to 's';
\-gp		Get recent posts' info including postid and title, support most recent 5 posts;
\-p		Use proxy to connect the internet, if '-proxy=' is not set, default proxy in perlwp file will be used;
\-proxy=s	Set the proxy setting, like 'http://user:pwd@xx.xx.xx.xx.:port'
\-info		Get the info about the blog, can be used to  connection;
\-help		Print this help info;


###NOTE:###

Please  set the default setting in perlwp file before usage, especially for $url and use lib path!
And thanks for Frontier::RPC2, great module. But to fix some minor issue in utf-8 encoding, I add 3 lines in Client part, and put it inside perwp dir as 'new' WPFrontier to make it more easy for users.
If there is any issue or suggestion, pls feel free to contact with shinemoon#gmail.com, thanks.


也许是敝帚自珍吧，每次打开上网本，然后几行命令行之后，pyroom全屏之后感觉世界都清净了，这样的感觉是我一直在许多离线编辑器上寻找却无法找到的。Linux Rocks！

PS. 几种典型的应用场景：


- 读取基本博客信息（主要是为了测试配置和连接情况）：perlwp -info \[-p\] \[-user=\] \[-pwd=\];


- 读取最近的博文信息（仅支持最近的五篇内容，主要是为了获取post id用于编辑博文）：perlwp -gp \[-p\] \[-user=\] \[-pwd=\];


- 新建博文，或者是在已有的本地草稿基础上继续编辑（具体是新建还是继续取决于是否有本地草稿存在，以及用户在提示符出现后的选择。）：perlwp -c \[-p\] \[-user=\] \[-pwd=\] \[-editor=\];



- 如果本地draft存在，此时会需要选择:Please select action:\[R(eopen)/D(elete)/C(ancel)\] 分别代表了在已有草稿上继续编辑，删除草稿重新开始以及取消返回的选项； 



- 编辑博文：perlwp -e=postid \[-p\] \[-user=\] \[-pwd=\] \[-editor=\];



- 如果本地draft存在，此时会需要选择:Please select action:\[D(elete)/C(ancel)\] 分别代表了删除草稿重新开始以及取消返回的选项；



- 删除博文：perlwp -d=postid \[-p\] \[-user=\] \[-pwd=\] ;

Posted By [PerlWP](//bitbucket.org/claudxiao/perlwp/wiki/Home')
