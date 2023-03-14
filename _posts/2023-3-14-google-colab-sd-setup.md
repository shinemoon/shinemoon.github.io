---
categories:
  - 技术
comment: 
date: '2023-3-14'
info: 
layout: post
published: true
sha: 95a74f7e74d5ddc5d24f5c3e28e53419033a781f
slug: google-colab-sd-setup
tags:
  - 技术
  - ' Google'
  - ' AI'
title: '基于Google Colab的Stable Diffusion搭建'
type: post

---

AI汹涌，就算不是靠这个吃饭，但是对技术的好奇心是永远不但能丢的，所以，简单的试了下基于Google的Colab的在线炼丹炉的搭建，非常粗浅，仅供入门参考。

## 预先准备
- 准备Google 账号，登录备用；
- 直接使用已经整理好的Colab的[高星索引:stable-diffusion-webui-colab][1] 

## 创建

只需要在stable-diffusion-webui-colab的Readme页面，根据[他整理的列表][2]，选择好你希望使用的Stable Diffusion的预备好的镜像；然后去点击表头的lite/ stable/ nightly 三种不同的图标，它们是直接链接到已经准备好的ipynb文件，会直接在[Google Colab][3]中打开、加载，三种版本区别就在于安装扩展不同，为了省事就用Stable吧。

## 运行

当导入了Colab之后，会看到有代码页面打开，此时只管无脑点击左上角的执行按钮，就会逐步执行所有的setup以及把Stable Diffusion 跑起来了——注意，服务会持续运行在浏览器页面打开的时刻（关掉就停了）

而执行到底部，会有服务器链接打印出来，告诉你登录哪个地址就可以直接登录到Stable Diffusion的WebUI。

对于不同的Setup，有时候会有些要求，例如，配置中需要你设置下登录密码、或者是Hugging Face的Token之类，这就具体情况具体分析了。

## 注意

Colab的使用和Python种种，就看各自自己的理解了，其实和Stable Diffusion本身没有强相关——而Colab的负荷目前看起来也都趋高，动不动就分配不到GPU了，所以如果认真想用，可能还是要考虑升级ColabPro吧。






[1]: https://github.com/camenduru/stable-diffusion-webui-colab
[2]: https://github.com/camenduru/stable-diffusion-webui-colab#-colab
[3]: https://colab.research.google.com