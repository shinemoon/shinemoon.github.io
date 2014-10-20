---
title:  Wordpress博客迁移方案之Tumblr篇
categories: 技术
tags: [wordpress, blog]
type: post
comment:  我得多爱折腾，不过是受M所托啊，谁让是终身保修来着~
info:
published: true
layout: post
---




对于那些挖好空间，但是因追(lan)求(yu)质(geng)量(xin)而几乎月更（甚至更懒）的博客作者来说，每年还花上几十上百的银子去维护一个博客空间，难免会有点鸡肋之感。

所以，找到一个尽可能便宜但是靠得住的免费博客方案（不含域名费用），还是颇有意义的事情。

针对码农或者爱好折腾的人，我从前写下的[Github Based的方案当然依旧实用][1](也依然是我本人博客的方案）；

但是当我遇到了普通人类关于「我能不能用那个什么jekyll」的问题后，我仔细的思考了下：即使我可以帮着迁移博客，向文艺青年传授分布式版本管理工具技巧的史诗级任务也是让我恐慌不已。

握紧拳头，看来是要寻找一个新的方案的时候了。

其实，事情并没那么复杂，选项也没有那么多—— 稳定、用户广泛、可以绑定域名、扩展性强、最好还能文艺实用兼备，舍Tumblr其谁？

决定既有，很快就是具体实现的工作了。

## 注册

这个工作，最简单了，特别是Tumblr好歹也还没有（至少目前没有）被墙掉。注册、验证，创建一个新Blog，如此而已。

哦， 防止万一有人不知道，链接：http://www.tumblr.com

## 如何导入导出wordpress的文章

wordpress的导出，就不需要讲解——就利用wp自带的导出功能，导出xml，备用。

比较微妙的是，怎样从wordpress的xml到tumblr的文章？ 很让我意外的是，居然没有特别现成的，官方的方案，tumblr官方看来也是相当的纯善。

Google之后的结论是，有一些开发者的工具，例如这位php直接从wordpress到tumblr的，但是，更广泛使用的（也是我这次采用的方法）却是间接的从Blogger到Tumblr的方案——主要原因是，这个方法里的几个关键工具都成熟度更高，更傻瓜一点，可是弊端是，blogger，需要翻墙——关于VPN的故事，那就不在这里赘述了，[「红杏」][3]不错。

[这篇文章就是最主要的参考文献][4]，坦白讲，不嫌读英文麻烦的话，大家可以跳过本文直接去读他的原文恐怕更加精准，特别是，他很细致的考虑了包括图片搬移的问题。而提到这个， 我不由再说一句，多利用标记语言，多利用第三方靠谱图床，才是一劳永逸的好办法，可以彻底的绕开搬移空间时的图片问题。

### 从wordpress到blogger

- 还是这样，首先，你得有个[blogger空间](www.blogger.com)，翻墙必须。
- 然后，到[这个地址](http://wordpress2blogger.appspot.com/)，依然需要翻墙，把wp中导出的xml上传进行转换，然后下载转换后的文件（有一点，该页面提到允许下载上限为1MB，但事实上，我这次用的大概有1.3M，也照样可以，可见约束并不严格，如果真的太大，估计要考虑把xml分段处理下再上传和下载了）
- 然后在blogger的dashboard里，选择'Import Blog Tool'选择转换后的文件上传，稍微（其实有点久了，当时 我等了大概十来分钟吧，总共300多篇文章）等待之后，你的blogger就可以完成导入；

### 从blogger到tumblr

- 再进入到这个[转换页面](http://www.bloggertotumblr.com/)， 填入你的blogger的RSS地址（记住是RSS，而不是首页，地址应该是类似 http://your_blogge_id.blogspot.com/feeds/posts/default?alt=rss ），和Tumblr的Blog地址，接受协议，点击下一步，就按照引导认证Tumblr权限并且开始转换了；
- 但是，如果你的帖子比较多，按照Tumblr的发帖限制（每天200篇），那么当天，你是无法完成所有的文章导入的，请按照错误出现后的提示，收藏这个页面地址，等到第二天（记住，时差），就可以继续前一天未完成的导入工作（这个进度保存恢复是在云端实现的，你只需要保存地址，在任何一个地方都可以继续，这点相当人性化）；
- 等到所有文章转换完毕，祝贺你，你已经可以抛开历史，开始新的旅程了。


## 如何绑定域名

绑定域名当然分为解析和Tumblr配置两方面：

域名解析侧，需要建立一条指向66.6.44.4的A记录（point A-record (IP address) to 66.6.44.4），这个具体使用的是哪家的域名解析服务，就请自行解决了；

另外，在Tumblr的博客配置的dashboard上进行如下步骤（[其实就是参考官方文档][5]）：

>- 点击顶部的设置图标（齿轮）
- 选中右边你希望配置的博客
- 在'username'部分的右侧选择'Use a custom domain'
- 输入域名；
- 点击'Test your domain' 进行测试，直到测试通过，配置的保存才被允许点击，这点要注意，即使修改之后的域名解析已经完成，等到生效往往需要很久，至少我这边等待了差不多一天之后，才终于可行；
- 点击'Save'


## 如何解决评论问题

鉴于Tumblr的逼格，一直对评论比较抵触，就连站内回复都是后面才逐步放开实现；目前要实现评论，最方便的做法，就是利用[Disqus的服务][6]。

在配置Tumblr主题时，有个"Disqus shortname"的选项，请在Disqus注册并且创建一个blog后，将对应的用户名填入这个选项并保存。

然后，

- 如果你足够幸运，选定的主题已经整合了Disqus，那么你不需要做任何事情，直接就可以用了；
- 如果主题缺省并未加入支持，那么就需要你自己编辑主题，加入Disqus的评论支持，简单讲就是在模版中嵌入Disqus的评论框架代码，非常简单。

参考[官方文档][7]:

- 在EDIT HTML后，把`<meta name='text:Disqus Shortname' content='' />`插入到head间；
- 然后搜索并且紧接在`{/block:Posts}`后，插入官方文档中提供的代码。
- 替换掉上述代码中的example，用你的本人的shortname代替

至此，完工。

## 结语

和Jeykll相比，利用Tumblr来搭建blog，方便，简单，直接，而且Tumblr的主题模版也自然大大的方便了普通用户的使用。

所以，除非和我一样是属于「强迫症」型的、希望一切数据都在自己手上、并且爱好折腾的人士之外，对于其他的用户，直到它可能「访问困难」的一天，都应该是一个很好的选择

——何况，Github本身也不是多安全的主儿。







[1]:http://mooninsky.net/from-wp-to-jekyll/
[2]:https://github.com/ideashower/Export-Wordpress-posts-to-Tumblr
[3]: https://chrome.google.com/webstore/detail/%E7%BA%A2%E6%9D%8F/heehjpdocpefckjobfgnfdbhoebhphkf?hl=zh-CN
[4]: http://howto.pui.ch/post/37850192094/how-to-migrate-your-wordpress-to-tumblr-including
[5]: https://www.tumblr.com/docs/en/custom_domains
[6]: http://disqus.com
[7]: https://help.disqus.com/customer/portal/articles/758168-tumblr-manual-installation-instructions
