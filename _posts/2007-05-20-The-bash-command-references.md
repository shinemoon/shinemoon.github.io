---
layout: post
title: Bash中的命令引用
categories:
- 技术
tags: [linux]
status: publish
type: post
info: 上海
published: true
meta: {}
---

其实很多脚本语言中都是这样的，但是我老忘记，备忘一下：

Compare listed commands:

echo pwd

echo "pwd"

echo `pwd`

显然，最后一个是我们需要的。
