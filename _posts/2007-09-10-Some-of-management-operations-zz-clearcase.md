---
layout: post
title: 'Clearcase的一些管理操作'
categories:
- 技术
tags: []
info: 上海
status: publish
type: post
published: true
meta: {}
---

ClearCase学习

今天上午参加了ClearCase的培训，并做了培训的整理，如下：

正常安装ClearCase的前提为：1. 不使用非Symantec的防火墙，2. 客户端所在电脑必须在公司网域内。

安装是否正常的判别方法：点击Control Panel中的ClearCase图标，检查四个Services是否均为正常运行。如果服务没有启动不是因为错误方法安装软件所致，则很有可能是默认的连接License的密码失效，需要到管理工具中的服务里重新设置Atria Location Broker服务的连接密码。

ClearCase的弱点：如果连接到License服务器的网络出问题的话，则所有的ClearCase客户端均无法操作。

 

下午得到了ClearCase Management的培训：

管理员登陆的流程为，在本机添加vob用户，切换至此用户并添加全局变量，随后打开ClearCase客户端即可。

管理员Import Project的方法为，先create一个view，然后mount一个vob并映射到一个盘符中的目录下，然后在cmd中输入：clearfsimport -r \[Source\] \[Destination VOB\]

ClearCase的实践

今天反复试验了ClearCase的所有命令，import、create view、check out、check in、create label、paste label、create branch with/without label、merge。并对管理过程做了个总结：管理员先import项目，让同事create snapshot view，然后同事就可以通过check out和check in工作了。如果要让同事工作的branch上，通常做法是管理员先create label，然后paste label，随后通过label来create branch，编辑好相应的config spec之后，将config spec mail给同事，这样当其check out文件时，该文件就create了一个需要的branch。当branch上的工作完成之后，管理员要将branch上的文件merge回main版本上。

工作在branch上的方法：（假设branch名为）

element \* CHECKEDOUT

element \* /main//LATEST

element \* /main/LATEST -mkbranch 

element \* /main/LATEST

Checkout后即可工作在的branch下了。

 

工作在某个tag上创建的branch的方法：（假设branch名为，tag为TEST）

element \* CHECKEDOUT

element \* /main//LATEST

element \* TEST -mkbranch 

element \* /main/LATEST

 
