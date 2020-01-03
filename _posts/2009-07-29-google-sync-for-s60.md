---
layout: post
title: Google Sync For S60
categories:
- 技术
tags: []
status: publish
info: 杭州
type: post
published: true
meta: {}
---

以前我在写关于goosync的文章时就提到，这只能算是一个临时性的替代措施，一旦Google Sync的服务完善，立马就会没有市场。很遗憾，这一天真的来到了。
  
也不知道具体什么时候，Google Sync终于放开了对S60系统的日历同步——而且更干脆，连实现方式也从最开始的使用S60手机的同步功能变成了借助Mail for Exchange，这样一来，不用说同步日历这个要求了，甚至也直接实现了近乎Push的实时性的同步。
  
具体步骤可以参见Google Sync的官网介绍

但是不幸的是，最近以来，从国内访问很多Google服务都会自动重定向到g.cn，Google Sync也是其中之一，所以我当时是拼命点stop才停在了Google Sync的页面，大家可以尝试一下，如果不行，就参照本文也可：


###基本步骤###

    
1. 推荐备份手机数据 - Backup your data         

2. 从nokia的网站下载Mail For Exchange软件并安装至手机 - [Download mail software](http://www.businesssoftware.nokia.com/mail_for_exchange_downloads.php)

3. 按照Google的指示来设置Mail for Exchange - [Set up Google Sync](http://www.google.com/support/mobile/bin/answer.py?hl=en&answer=147951) (可以参照下文）


简单说就是：备份数据 - 下载Mail For Exchange -设置mail for exchange的同步信息。
  
下载安装都很简单，如同一般的软件。
  
安装好之后，就会开始进行账户设置，同样借用官方说明：

开始之前:      

强烈推荐使用PC Suite或其他管理软件来备份手机数据。       

请确认你的手机型号是Mail for Exchange所支持的，并且确认你的Mail for Exchange是最新版本。接下来请按照下面的步骤配置：
      
1. 打开手机中Mail for Exchange的目录，并且运行Mail for Exchange的程序。
      
2. 当询问你是否要创建新的档案时，选择Yes。
      
![image](http://i340.photobucket.com/albums/o350/claudxiao/sync_147951d_sync_create_en.png) 
      
3. 然后如下步骤配置档案：
      
![image](http://i340.photobucket.com/albums/o350/claudxiao/sync_147951b_sync_connections_en.png) 
      
连接
             
-Exchange 服务器: m.google.com         
-安全连接: Yes          
-接入点: （自行选择）          
-漫游时同步: （自行选择）          
-使用默认端口: Yes        
       
![image](http://i340.photobucket.com/albums/o350/claudxiao/sync_147951c_sync_password_en.png)                   

证书
        
-用户名: 你的gmail邮箱全名, e.g. jon@gmail.com         -密码: Gmail密码          -域: 留空                  
        
同步日程
        
- 该设定用于决定何时启动同步. 如果使用始终打开，可以保证数据的即时性, 但是显然会更加耗电.        

![image](http://i340.photobucket.com/albums/o350/claudxiao/sync_147951a_sync_calendar_en.png)&#160;        

日历
        
- 同步日历: 是或者否        

- 同步日历回溯: 自行选择         初次同步: 决定第一次同步时对于手机端和网络端的内容的取舍.        
                  

任务
        
- 同步任务: 否(当前不支持)                 
        

联系人
        
- 同步联系人: 是或者否         初次同步: 决定第一次同步时对于手机端和网络端的内容的取舍.        
                  
邮件
        
- 同步邮件: 否(当前不支持)        
                     
  
之后，一切就顺风顺水，无论是日历还是联系人，都可以非常方便的进行自动的同步了，而第三方的类似服务，在这个情况下，显然只有被无情抛弃一途了。而Google的这一步，让人不由的又开始期待，会不会有那么一天，它再顺便把‘Mail'的同步也直接做进去呢？
