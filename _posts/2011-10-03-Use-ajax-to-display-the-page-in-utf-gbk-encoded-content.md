---
layout: post
title: 在UTF页面利用AJAX显示GBK编码内容
categories:
- 技术
tags: []
status: publish
info: 杭州
type: post
published: true
meta: {}
---
本地编码utf-8, 服务器gbk，ajax怎样弄才能无乱码显示？

折腾了一下午，最后其实就是一句话，果然是大道希行。	

xmlHandler.open("GET", txtUrl, false);	//GBK编码解决	

if(xmlHandler.overrideMimeType)	{
	xmlHandler.overrideMimeType('text/xml;charset=gbk');	
}	

xmlHandler.send();
