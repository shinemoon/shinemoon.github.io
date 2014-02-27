---
title: WD My Cloud修砖纪实
layout: post
categories:
- 技术
tags: []
info: 杭州
published: true
---

> 「不做死就不会死」—— 

作为前述的Jekyll的后续故事，本来想在家里的这块「My Cloud」上做一个自动定时检查文章更新，然后build-push的环境（这样一来，我在任何地方只要通过WD2Go的服务上传一篇文章到硬盘里，理论上家里的My Cloud就可以帮我发布），不料熬到深夜的我，在装bundler的时候脑子一昏，居然把一些核心库给删掉了，而且第一时间没有反应过来，重启了My Cloud。

很自然，变砖了，而且是硬邦邦的砖（相对于论坛上谈到的有ssh但是没有正确UI的soft-brick来说），连网络都没法连接了。

多少年没有写过什么「技术」、「开箱」、「指南」之类的文章了，但是考虑到WD My Cloud是个不那么大众而且相对比较新的东西，国内网上似乎也没看到比较详细的介绍。那么我就姑且写下自己未必成功的尝试吧。

参考文章是从WD的官方论坛上获得的：[How to unbrick a totally dead My Cloud](http://community.wd.com/t5/WD-My-Cloud/How-to-unbrick-a-totally-dead-My-Cloud/td-p/651195/highlight/true)，虽然贴主是提问的，但是几位答复者，特别是[sammarbella](http://community.wd.com/t5/user/viewprofilepage/user-id/241409)的好几篇热心回复，是我这次尝试的源头，我也就默默在这里祝他好人一生平安……

## 准备工作

思路很简单，如下几步：

- 先寻求WD的官方支持（当然不能说是ssh搞坏的，就当是我升级断电了吧……），看看官方有没有什么好办法；`官方果然一天多没理我，等了两天，回复了一封一看就是自动生成的「建议寻找代理或者服务商返修」的官话邮件，算了，自己动手吧。`
- 开箱，拆出硬盘；
- 通过SATA/USB的硬盘盒接到电脑上（Mac & Win 均备选），按照论坛帖子进行云盘OS的恢复写入；
- 如果恢复成功，装回去。

看上去好像相当简单——才有鬼啊。

## 拆机

拆机到第一步就遇到很现实的问题，网上找不到拆机的教程，我全网搜索唯一看到的是在SMZDM上有位开箱兼拆解的还是跳过过程，直接给出了结果图，更不用说那次拆机还是破坏性拆机——机壳的卡子全部都损坏了。至于Google和Youtube上只有Mybooklive的拆机教程和视屏。

所以，在我自己所见范围内，我这是「全球」（我能找到的）第一份拆机的记录，以及第一份「无损」拆机（我在臭屁什么啊？）……好紧张。

首先是未拆之前，光线不好加上手机拍摄，画质什么的，环境什么的请忽略：

![Before](http://i340.photobucket.com/albums/o350/claudxiao/WP_20140227_zpscdab27f1.jpg)

接下来是各种窥看和猜测，还有对外观接缝的试探，最终定下了解决方案，那就是，针对这种无螺丝的外壳组装方式，关键就是找对方向、找到着力点。很显然，方向即使朝着面板正面对外拉，着力点反而是最难的，那就要自己创造：用绳子外加镊子，终于实现了对机壳的捆缚，然后剩下的就是用废信用卡略微撬松接缝，最后用吃奶的力气来拉吧——

当出现下面一幕，盖子被终于拉出了一小节的时候，我的心情之激动简直无以言表。

![pull](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402271_zps74513ff5.jpg)


模具工艺应该说还是不错的，完全是利用了滑槽和卡扣实现了不错的外壳安装机制。

![pulling](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402272_zps0973cd7c.jpg)

这就是SMZDM的帖子里被全数毁坏的卡扣，在这里，是完好的：

![kakou](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402274_zps4bf7fcef.jpg)

传说中的超值的2TB红盘：

![red](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402273_zps74a769a1.jpg)


接下来的事情就比较简单了，无非咬咬牙毁掉保修的封条，下螺丝，包括装在硬盘两侧的防撞的橡胶帽——稍微注意的就是把硬盘和控制板从塑料外壳上拿下来的时候，注意下角度，别把那几个接口给挂掉了，以及那个指示灯的部位的小塑料片看上去略脆弱，须留心。

![continue](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402275_zpsf453997a.jpg)

另外，控制板的SATA接口是反扣上去的，拆的时候，也要稍微注意一些。

![continue](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402278_zps0271d6db.jpg)

下面是全家福，包括工具和散件——好了，打包收好，等待明天借来3.5'的硬盘盒，准备刷系统了。

![all](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402277_zps9aadfda3.jpg)


## 刷机

接下来就是要如何去把系统给刷回去这个严肃的问题了：

软件上，先去WD的官网下载最新的固件更新，然后用解压缩的工具找到<解压后的目录 >/data/CacheVolume/upgrade/rootfs.img文件，复制到比较方便的地方备用。

然后，先从同事手中借到了「利器」，SATA硬盘座：

![Dock](http://i340.photobucket.com/albums/o350/claudxiao/WP_20140228_zps3b7649a0.jpg)

接上硬盘，插上了我的MacBook Air——当然，首先就是个不能识别硬盘的下马威，这个也是意料之中的事情了；

可是问题来了，在我参考的帖子里，很多基于GUI的方法都是用的是Gparted或者是Disk（Ubuntu），可是OSX呢？先试了下系统的磁盘工具，果然被告知无法恢复磁盘——因为它当然看出来源文件不是个合法的OSX的img了。

![disk](http://i340.photobucket.com/albums/o350/claudxiao/5C4F5E555FEB71672014-02-27112203PM_zps6407c179.png)

都到这一步了，怎么能够被这个拦住，作为菜鸟的我仔细爬了爬楼，才确认用dd就可以了，于是开工：

先`diskutil list`看看磁盘状态，找到硬盘上放系统分区的两个盘符，很明显，就是类型是Linux_RAID, 大小约为2G的两个分区了；

![dist](http://i340.photobucket.com/albums/o350/claudxiao/5C4F5E555FEB71672014-02-27115724PM_zpscd574eaa.png)

接下来，用`sudo dd if=/Users/iclaud/rootfs.img of=/dev/disk1s1`和`sudo dd if=/Users/iclaud/rootfs.img of=/dev/disk1s2`把系统刷回到两个系统分区；

![image](http://i340.photobucket.com/albums/o350/claudxiao/5C4F5E555FEB71672014-02-27115735PM_zps6ee347d4.png)

好了，能做的我都做了，接下来就看效果了，我的心情异常的忐忑：

![try](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402282_zps6578a511.jpg)

先接上控制板，插上电源和网线，上电，一阵硬盘的读取之后，我反复的刷着webpage，终于，蓝灯亮起，同时，管理界面重新出现了！

![ui](http://i340.photobucket.com/albums/o350/claudxiao/5C4F5E555FEB71672014-02-28120427AM_zpsb497ac33.png)

大功告成，可以装机了——


## 装机

不要以为装就是毫无技术含量的事情，两个地方需要注意——首先是控制板和硬盘间起到支架作用的那三个小黑塑料柱子，怎么放进去（在已经插上控制板之后）就是件比较考验手艺的事情，一把称手的镊子必不可少，此外，千万仔细看拆机时的照片，那左右一共四个橡胶减震头，装的位置要正确，否则，很可能就没法装上去，还是要返工。

其次，最后装进盒子的时候，最好先把左侧（靠近各类接口那侧）的橡胶头拔下来（当然，螺丝在硬盘上）先塞到壳子的两个槽里放妥当，然后，再把只剩下金属轴的硬盘塞进去，否则，一味带着橡胶头子想往盒架上塞，简直是Mission Impossible.
![image](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402281_zps4cb90605.jpg)

终于，费了九牛二虎之力，算是基本还原——没有白折腾啊，下次再也不能手贱乱点「Yes」了。

![done](http://i340.photobucket.com/albums/o350/claudxiao/WP_201402283_zpsbf689094.jpg)

## Fin
