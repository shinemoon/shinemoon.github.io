---
layout: post
title: Hotmail终于开放了全球的POP3收信
categories:
- 技术
tags: []
status: publish
info: 上海
type: post
published: true
meta: {}
---

继前段时间向11个地区（不包括中国）开放了POP3功能之后，[微软终于宣布Hotmail向全球用户开放了POP3](http://www.cnbeta.com/articles/79176.htm)——这个举动已经晚了太多了。
  
按照网友评论的说法，‘动作太慢，就等着喝点残汤吧。’，记得刚接触网络时，说起邮箱，Hotmail总是最先被想起的服务。到了今天，出于历史习惯而依然强大的Yahoo在前，上升势头明显而且口碑、体验绝佳的Gmail在后，Hotmail暮气沉沉的形象早在我心里扎下了根。
  
使用Hotmail对我来说，唯一的原因就是我的MSN帐号是绑定的Hotmail，所以有些邮件必须要用hotmail收发，每到这个时刻，就是想骂人的时刻。因为前两年的Hotmail的服务器在国内访问，要多别扭，就有多别扭；而后对于用户界面几次让我很不喜欢的改版更是蹩脚。
  
但是没有办法，Hotmail牛气的一直拒不开放外部POP收信，如果确实想外部收信，那也得用微软自家的工具，例如Live Mail。但是，微软的东西向来就不是轻便的主。我明明应该开个网页（例如，Gmail）就能搞定的事情，非要去装一个尾大难掉的Live Mail，专职服务于这个邮箱，实在没有这个兴趣。
  
所以，得知这个消息后，我做的第一件事情，也许就是微软最不愿见的事情——设置了Gmail来收发Hotmail……设置信息如下：

POP 服务器: pop3.live.com （端口 995）    

需要 POP SSL？: 是的     

用户名: Windows Live ID, 比如：[xyz@hotmail.com](mailto:xyz@hotmail.com)     

密码: 对应 Windows Live ID 的密码     

SMTP 服务器: smtp.live.com （端口 25）     

需要身份验证？: 是的     

需要 TLS/SSL？: 是的 

最后，让所有收自Hotmail的邮件带上HOTMAIL的Label，一切OK。终于再也不用去登录那个别扭的Hotmail了。
  
ps. 似乎hotmail设置的收取时间最短是14分钟，所以会在Gmail的收取log中看到一些错误，这些都没有关系。

