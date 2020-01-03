---
layout: post
title: Sed 的典型应用
categories:
- 技术
tags: [linux]
status: publish
info: 上海
type: post
published: true
meta: {}
---

一、 批量文件更名：

<code>
for curfile in \*; do    
mv $curfile `echo $curfile | sed -e s/old/new/g `    
done
</code>

二、 文件内容修改：

<code>
sed -i s/oldstring/newstring/g `grep oldstring -rl yourdir`
</code>
