

2022-04-24:

时间过去也真是快，几年时间之后，所有曾经预置和努力过的评论系统都已经无效了；最后来加进去的Livere虽然可以用，但是速度并不理想，而且，会随机的加入（很难看的）广告块；最后还是下定决心改成了[Gitalk](https://github.com/gitalk/gitalk)，简单说来，就是利用Github的issue体系来做评论系统，就是利用一个镜像的repo里的issue，用issue来作为所link的原文章的评论，缺点主要有两个

- 必须要登录Github才能留言；（这个没法规避了，只能说，给有心人吧）
- 每篇文章都需要管理员（一般就是blog的拥有人)来刷新blog文章页面之后，触发一个建立issue的动作；

手动初始对于新文章来说一般不是问题，因为Jekyll的用户我想大部分都会习惯于写完之后至少看下效果吧？而只要打开在线页面，都会自动触发一个初始化评论的动作，所以我甚至原本打算做一个github action来自动触发的想法，后来也都放弃了，觉得性价比太低了，没有太多必要；

可是，这一个问题对于有着许多老的文章（比如本人就有六百+的文章）的用户来说，就比较痛苦了。总不能每篇都去点开看吧。

所以，我就在这里放了一个python脚本, *autoissue.py* （在https://github.com/shinemoon/shinemoon.github.io的根目录下）, 只要安装一下requests的包之后，在本地的repo内，执行 `python autoissue.py scanAllPosts`这个指令，就会自动扫描_posts目录，然后试图根据文章信息创建所有的评论issue（当然，会自动检查是否已经存在），其中主要参考借鉴了[LinuxShell的这篇文章和代码](https://www.lshell.com/post/use-github-action-and-python-to-automatically-initialize-gitalk-comments/)

当然，还有就是需要把根目录下的config.ini.template复制一个config.ini并且把配置里的内容换成自己的配置,其余的配置大部分不变，只是注意，

- repo_name指的是评论系统的repo，
- 域名要有最后的/，
- 以及，千万记得不要把包含了自己token的本地config文件不小心放到了git内，务必记得.gitignore里筛出。

当然，如果并不是和我的Jekyll一模一样，例如，label生成的规则不同、link产生的规则不同，那就需要到python文件里自己酌情修改一下了。

目前来说比较满意。


2020-07-10: 

将今日诗词从hardcoding改为了第三方插件性质的实现，为后面可选摘录做准备；同时rebase了repo，变成了一个。

2018-11-14: 

替换了子标题内容，谢谢[今日诗词](https://www.jinrishici.com/#) 的开放接口，会按照天气、时间和地点推荐随机的诗词。

---- 

> 从NexT修改而来的个人Blog主题, 详细参见下面引用部分：
> 
># NexT
>   
>   > 精于心，简于形
>   
>   NexT 是由 [Hexo NexT](https://github.com/iissnan/hexo-theme-next) 移植而来的 Jekyll 主题。<!--commit: f951075d9b739d26b42472431995fa68d08796aa-->
>   
>   <a href="http://simpleyyt.github.io/jekyll-theme-next/" target="_blank">在线预览 Preview</a> | <a href="http://simpleyyt.com" target="_blank">Yitao's Blog</a> | <a href="http://theme-next.simpleyyt.com" target="_blank">NexT 使用文档</a> |  [English Documentation](README.en.md)
>   
>   [![Join the chat at https://gitter.im/simpleyyt/jekyll-theme-next](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jekyll-theme-next/lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
>   
>   ![NexT Schemes](http://iissnan.com/nexus/next/next-schemes.jpg)
>   
>   
>   ## 浏览器支持 Browser support
>   
>   ![Browser support](http://iissnan.com/nexus/next/browser-support.png)
