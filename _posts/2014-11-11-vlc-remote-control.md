---
title: 命令行下怎样远程控制VLC播放
categories: 技术 
tags: [Linux]
type: post
comment: 
info:
published: true
layout: post
---

开宗明义，在Headless （ i.e. without a monitor or input device）的服务器（例如，各类嵌入式「玩具板子」）上如果架起VLC进行多媒体播放，怎样才是最方便的控制方式？

同时，因为希望是可以脚本控制，所以最好是可以做到非互动式的指令。

如下是简单的步骤：

## 使能VLC的Remote Control接口

VLC实际上拥有灵活强大的控制方式，由于我们上来就限定了Headless，那么命令行显然是先决条件，VLC文档中已经列出了支持的几种Remote方式：

- rc interface
- ncurses interface
- telnet interface

考虑到三者中rc应该是最强大和灵活的（ncurses需要configure，telnet更多的是互动型，何况rc本身就可以支持telnet访问），我们就focus在rc 接口上。

使能方法非常简单，调用vlc的时候，用：

`cvlc -I rc --rc-fake-tty --rc-host <ip>:<port>`

选项     |意义           |
-------|-----------|
'-I rc'| 启动rc接口；
'--rc-fake-tty'| 强迫将标准输入当做tty
'--rc-host' | 选定的监听地址和端口
    
注意：如果需要局域网内访问，请填写本机ip，如果只要本机访问，用localhost就可以了

得到如下信息（忽略那些错误吧，毕竟Headless么，很多接口对VLC来说都缺失，但是不影响使用）

> cvlc -I rc --rc-fake-tty --rc-host localhost:8888        
VLC media player 2.0.3 Twoflower (revision 2.0.2-93-g77aa89e)        
[0x11eed70] inhibit interface error: Failed to connect to the D-Bus session daemon: Unable to autolaunch a dbus-daemon without a $DISPLAY for X11        
[0x11eed70] main interface error: no suitable interface module        
[0x11eed70] main interface error: no suitable interface module        
[0x10858f0] main libvlc error: interface "globalhotkeys,none" initialization failed        
[0x11eed70] [cli] lua interface: Listening on host "localhost:8888".        
        

## RC 接口指令

直接借助帮助文件, 可见还是非常强大的：

> +----[ CLI commands ]        
| add XYZ  . . . . . . . . . . . . . . . . . . . . add XYZ to playlist        
| enqueue XYZ  . . . . . . . . . . . . . . . . . queue XYZ to playlist        
| playlist . . . . . . . . . . . . .  show items currently in playlist        
| search [string]  . .  search for items in playlist (or reset search)        
| sort key . . . . . . . . . . . . . . . . . . . . . sort the playlist        
| sd [sd]  . . . . . . . . . . . . . show services discovery or toggle        
| play . . . . . . . . . . . . . . . . . . . . . . . . . . play stream        
| stop . . . . . . . . . . . . . . . . . . . . . . . . . . stop stream        
| next . . . . . . . . . . . . . . . . . . . . . .  next playlist item        
| prev . . . . . . . . . . . . . . . . . . . .  previous playlist item        
| goto, gotoitem . . . . . . . . . . . . . . . . .  goto item at index        
| repeat [on|off]  . . . . . . . . . . . . . .  toggle playlist repeat        
| loop [on|off]  . . . . . . . . . . . . . . . .  toggle playlist loop        
| random [on|off]  . . . . . . . . . . . . . .  toggle playlist random        
| clear  . . . . . . . . . . . . . . . . . . . . .  clear the playlist        
| status . . . . . . . . . . . . . . . . . . . current playlist status        
| title [X]  . . . . . . . . . . . . . . set/get title in current item        
| title_n  . . . . . . . . . . . . . . . .  next title in current item        
| title_p  . . . . . . . . . . . . . .  previous title in current item        
| chapter [X]  . . . . . . . . . . . . set/get chapter in current item        
| chapter_n  . . . . . . . . . . . . . .  next chapter in current item        
| chapter_p  . . . . . . . . . . . .  previous chapter in current item        
|         
| seek X . . . . . . . . . . . seek in seconds, for instance `seek 12'        
| pause  . . . . . . . . . . . . . . . . . . . . . . . .  toggle pause        
| fastforward  . . . . . . . . . . . . . . . . . . set to maximum rate        
| rewind . . . . . . . . . . . . . . . . . . . . . set to minimum rate        
| faster . . . . . . . . . . . . . . . . . .  faster playing of stream        
| slower . . . . . . . . . . . . . . . . . .  slower playing of stream        
| normal . . . . . . . . . . . . . . . . . .  normal playing of stream        
| rate [playback rate] . . . . . . . . . .  set playback rate to value        
| frame  . . . . . . . . . . . . . . . . . . . . . play frame by frame        
| fullscreen, f, F [on|off]  . . . . . . . . . . . . toggle fullscreen        
| info . . . . . . . . . . . . .  information about the current stream        
| stats  . . . . . . . . . . . . . . . .  show statistical information        
| get_time . . . . . . . . .  seconds elapsed since stream's beginning        
| is_playing . . . . . . . . . . . .  1 if a stream plays, 0 otherwise        
| get_title  . . . . . . . . . . . . . the title of the current stream        
| get_length . . . . . . . . . . . .  the length of the current stream        
|         
| volume [X] . . . . . . . . . . . . . . . . . .  set/get audio volume        
| volup [X]  . . . . . . . . . . . . . . .  raise audio volume X steps        
| voldown [X]  . . . . . . . . . . . . . .  lower audio volume X steps        
| adev [X] . . . . . . . . . . . . . . . . . . .  set/get audio device        
| achan [X]  . . . . . . . . . . . . . . . . .  set/get audio channels        
| atrack [X] . . . . . . . . . . . . . . . . . . . set/get audio track        
| vtrack [X] . . . . . . . . . . . . . . . . . . . set/get video track        
| vratio [X] . . . . . . . . . . . . . . .  set/get video aspect ratio        
| vcrop, crop [X]  . . . . . . . . . . . . . . . .  set/get video crop        
| vzoom, zoom [X]  . . . . . . . . . . . . . . . .  set/get video zoom        
| vdeinterlace [X] . . . . . . . . . . . . .  set/get video deintelace        
| vdeinterlace_mode [X]  . . . . . . . . set/get video deintelace mode        
| snapshot . . . . . . . . . . . . . . . . . . . . take video snapshot        
| strack [X] . . . . . . . . . . . . . . . . . set/get subtitles track        
|         
| vlm  . . . . . . . . . . . . . . . . . . . . . . . . .  load the VLM        
| description  . . . . . . . . . . . . . . . . .  describe this module        
| help, ? [pattern]  . . . . . . . . . . . . . . . . .  a help message        
| longhelp [pattern] . . . . . . . . . . . . . . a longer help message        
| lock . . . . . . . . . . . . . . . . . . . .  lock the telnet prompt        
| logout . . . . . . . . . . . . . .  exit (if in a socket connection)        
| quit . . . . . . . .  quit VLC (or logout if in a socket connection)        
| shutdown . . . . . . . . . . . . . . . . . . . . . . .  shutdown VLC        
+----[ end of help ]        

## 如何访问：

实际上，在一些[讨论][1]中看到，如果只是需要本机访问,更高效的办法是借助一个unix socket文件，从而通过socket文件来访问，简单说就是将上面提到的-rc-host选项变成-rc-unix然后用一个文件作为输入；

这样可以用类似于形如下面指令的方法来模拟socket访问 (作者以OSX为例，应当是没有问题的）：

`echo normal | nc -U /Users/vlc.sock`

我的例子，Debian中，nc似乎是不适用，更多人推荐用socat （需要安装）

`echo “pause” | socat – UNIX-CONNECT:/Users/vlc.sock`

上面可以理解成将管道化之后的ECHO字符向这个Unix的Socket发送。可是在我这里死活都会遇到文件connection refused，作为菜鸟，实在无力解决，特别是看到有强者遇到类似问题交叉比较得出可能和特定版本的kernel stock存在bug有关之后，不管看不看得懂，我都理直气壮的放弃了——直接转向了上面提到的host:port的方案。

所以：

### OSX

如果是互动式，直接 `nc <host> <port>`，就可以进入这个接口界面了:

>  $ nc 192.168.199.105 8888        
VLC media player 2.0.3 Twoflower        
Command Line Interface initialized. Type `help' for help.        
> $ **status**        
( new input: file:///home/user/test.mp3 )        
( audio volume: 256 )        
( state playing )        
> $ **info**        
+----[ Stream 0 ]        
|        
| Bitrate: 160 kb/s        
| Type: Audio        
| Channels: Stereo        
| Sample rate: 44100 Hz        
| Codec: MPEG Audio layer 1/2/3 (mpga)        
|        
+----[ end of stream info ]        

如果不需要互动：

参考上节：

`echo status | nc -w 0 <ip> <port>`

-w是指示说该命令之后，立刻退出，实际上OSX下并不一定需要，只是为了和下面Linux对照一下。


### LINUX

大致相同，区别只是在非互动式下，

`echo status | nc -q 0 <ip> <port>`

两者区别只是一个用了' **w**ait'之意，另外一个是' **q**uit'罢了，想想还挺风趣....风趣个妹啊，这不是折腾跨平台用户吗？！


##结论

至此，该问题解决，不论是想在远程控制无输入（显示）设备上的播放，还是想用脚本对其他线程的VLC播放进行自动化的干预控制，都不成问题了。

——怪不得有那么多人喜欢用VLC啊，我恍然。


[1]: http://n0tablog.wordpress.com/2009/02/09/controlling-vlc-via-rc-remote-control-interface-using-a-unix-domain-socket-and-no-programming/




