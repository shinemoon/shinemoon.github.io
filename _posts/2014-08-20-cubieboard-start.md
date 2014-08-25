---
title:CubieBoard入手相关 
categories: 技术 
tags: [ARM, 嵌入式, Linux]
type: post
comment: 
published: true
layout: post
---
![overview] [a]

*图片为Radax Rock，并非Cubieboard，是Cubie创始团队基于瑞芯微的RX系列开发的类似的下一代开发板*

NOTE: 本文主要聚焦CubieBoard相关的特殊内容，而对于类似Android或者Linux本身相关的内容不做过多展开和深入。

## 入手安装

缺省安装是android，在没有扩展键盘鼠标以及不方便接入hdml显示器（电视）的时候，开荒逻辑显然是：

1. TTL串口连接调试；
2. 配置以及获取网络信息；
3. SSH

而且明显的，android不满足我的操作要求，必须先刷成linux，而且server版尤佳。

因此下面的部分也就是照这个思路进行的。

![board][d]

### TTL线连接

- 无显示器情况下，TTL线连接，白线对应TX，绿线对应RX，黑线对应GND，** 据教程说明，红线悬空，否则会有烧板可能**;
- 需要ttl支持的软件，例如putty等，osx下使用minicom（需要安装）；
- 配置好minicom之后，要先打开minicom（port选择为/dev/cu.usbserial),然后打开电源，当然这之前，usb线得要接好，这样就可以看到启动的全过程了；
- 启动之后，直接是root账号登录了，可见cb为了开发者方便，上来就是直接裸奔，这个不重要，反正是要刷掉这个android的。

### Cubian 刷机 

细节参见[官网] [1], 说的应该很清楚了，最花时间的部分却反而是我因为没有sd卡读卡器而几经周折的来回换电脑的经历.

Cubian虽然是玩家自制，但是从完备和易用上远远超过了官方的版本，至少那个LED灯靠摩尔斯码显示ip地址的想法真是让人绝倒，绝对的上档次。


插上无线网卡(我用的也是官方推荐的水星迷你无线网卡）之后，需要配置wifi（目前阶段且只管本身的）；
	
+ 确保工具安装`sudo apt-get install wpasupplicant`, 因为iwconfig只能处理WEP，而对于WPA，必须需要wpasupplicant来处理，不过Cubian已经预装了；
	+ 利用`sudo iwlist wlan0 scan `来扫描wifi，届时需要处理提取ssid和加密方式来提示用户，目前暂时先不在意，直接填写家庭wifi以便调试；
	+ 利用`wpa_passpharase <essid> <password> > /etc/wpa_supplicant.conf`生成配置文件；
	+ > **本方法未成功**，有错误，可能是wpa_supplicant 本身问题，`sudo wpa_supplicant -B -iwlan0 -c/etc/wpa_supplicant.conf -Dwext && sudo dhclient wlan0` 来打开wifi, 于是采用了下面的方法；
	+ 采用类似[Cubian教程的方法][10],
		- 修改 /etc/network/interfaces文件，添加如下内容(其中psk请从前面passpharse中生成的文件中读取）
>allow-hotplug wlan0    
> iface wlan0 inet dhcp    
>   wpa-ssid mynetwork    
>   wpa-psk 000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f    
		
- `ifup wlan0` 启用wifi


Wifi正式OK，那么终于可以移动使用了。

但是，如果仅这样，重启之后，wifi依然是disable的，需要手动打开（这对我headless的solution完全没有帮助），即使按照Cubian文档做了（即，添加auto wlan0在文件里，也无补于事）；最后找来找去，还是在/etc/rc.local里加上了这两句:

`/sbin/wpa_supplicant -c /etc/wpa_supplicant.conf -D wext -dd -i wlan0 -B`    

`dhclient wlan0`

才算是解决了重启的问题。Wifi正式OK，那么终于可以移动使用了;

唯一不太爽的是，不知道为什么如果在有线连接的情况下，本来有线和无线的ip都是获取的，但是如果当中拔掉网线，反而无线也会失效，非要重启（因为我是headless的server版...无显示器、无键盘), 看看以后能不能解决吧。

### Lubuntu 刷机 (弃用)

参考[官方连接] [1]

几点note:

- 可以选择刷机到sd卡或者是nand flash，作为强迫症的本人，当然选择刷NAND了, 有[官方教程][5]；
- 那么，就需要全志的[官方工具LiveSuite了] [2], 很欣慰的是，居然是有Mac版本的，对Allwinner一下子很有信心了；
- 安装与打开都非常傻瓜
 ![livesuite] [3]
- 接下来，就是选择image了，如前所述，Lubuntu Server 就是选择(382M的image), 原来的UbuntuOne的空间失效，似乎很难找，不过总算是找到了, [官方有备份][4];
- 如果一切顺利，大家应该就可以按照类似下面Windows上的步骤刷机了...为什么我会切换到Windows下呢?

因为过程中却沮丧的发现，刷image遇到了'Wait for fes device timeout ..' 的问题，搜索之后，疑似是Cubieboard对usb3.0有点兼容问题(也有说法是有点挑usb口），不得已只好切换到Window7的电脑上:

过程中要说的几点：

1. 板上不需接电源（接了反而不行）；
2. 先打开phoenixSuite，选择好image,而且刷之前，最好先接好板子，至少把板子的驱动确认能识别；
3. 再按住FEL按键（在usb口底部）的同时，插上usb线；
4. PhoenixSuite会跳出提示，等到开始刷机再松开按键；

自然等待刷机完成,大概两分钟左右。再次上电，就可以看到成果了：

![lubuntu][6]

唯一比较讨厌的是，这之后，LED2（蓝灯）闪烁个不停，搜了下，似乎是CPU心跳的显示，这...暂时拿它没办法，研究之后再说吧。

> These are blue LED1 meaning heartbeat and green LED2 on cb1 and cb2

附上[Lubuntu的材料][7];


在封箱之前，最重要的事情，其实就是要确保网络(至少有线网络吧?）和ssh是好的, 这个就是基本的Linux知识，不再赘述了。

不过依然有几个要点：

1. 如Guide所说，下面这一步是不可少的（对我如此）：`$dhclient eth0`
2. 因为官方image是13.03的版本， 所以至少apt-get的源列表的quantal有许多不对了，把/etc/apt/source.list中的quantal改成utopic就可以解决很多源找不到的问题了；

**NOTE**: 
在源解决后，发现其实更严重的问题是apt-get依然有Bus Errorpackage list ... 0%的问题存在，我没有找到合适的解决方法，几个搜索得来的解法都未能成功，只得改变主意转向了Cubian，这个基于Debian的针对Cubieboard的版本；


### 装外壳

本来似乎应该更早一点，但是当时担心有些东西需要先开盖整，装好以后太麻烦，所以放在这一步，壳子用的是官方淘宝上的黑白壳。

![break]  [b]

必须说，模具本身谈不上精美，但是还是挺准确的，板子一步按到位，没有出现任何接口和外壳开口的错位情况；只有那个滑盖有时候会蹭到黑色贴纸，产生刮痕。

并且TTL口也无法引出（当然没法了，放置在板子中间，而且是分离式的插线），所以，为了以防万一，装外壳之前，建议先好好的试试ssh是否OK，否则又要来回折腾了。

盖上之后，基本上对外也只有几个接口处是通风的，老实讲我对散热略有担心——虽然配了块小散热片，我也贴在了A10上，而且我也没打算真的去当作视频盒子用（都装Server版了），不过，还是尽量划开滑板，留出了SATA接口的那块天窗，聊做散热吧。
![comparison] [c]

至此，一个卡片大小的，debian based的干净电脑算是攒好了，就看之后能有什么可折腾的了。

----



[1]: http://docs.cubieboard.org/tutorials/cb1/installation/cb1_lubuntu_nand_install
[2]: http://linux-sunxi.org/LiveSuit
[3]: http://i340.photobucket.com/albums/o350/claudxiao/livesuite_zpsf3e2334b.png
[4]: http://dl.cubieboard.org/software/ubuntuone/public/cubieboard/cb_a10_ubuntu/
[5]: http://docs.cubieboard.org/tutorials/cb1/installation/cb1_lubuntu_nand_install
[6]: http://i340.photobucket.com/albums/o350/claudxiao/livesuite_zpsf3e2334b.png
[7]: http://docs.cubieboard.org/tutorials/common/begining_on_lubuntu
[8]: http://cn.cubian.org

[a]: http://i340.photobucket.com/albums/o350/claudxiao/Rock_zps37e999f5.jpg
[b]: http://i340.photobucket.com/albums/o350/claudxiao/cbbreakdown_zps53e9b662.jpg
[c]: http://i340.photobucket.com/albums/o350/claudxiao/cbcomparison_zps3936900d.jpg
[d]: http://i340.photobucket.com/albums/o350/claudxiao/cubieboard_zpseebcbc43.jpg

[10]: https://github.com/cubieplayer/cubian/wiki/%E4%B8%8A%E6%89%8BCubian
