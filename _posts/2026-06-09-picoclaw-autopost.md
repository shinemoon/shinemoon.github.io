---
title: 今天用 picoclaw 自动发布了一篇文章
date: 2026-06-09 13:10:15 +0800
layout: post
published: true
category: 折腾记录
tags: [picoclaw, blog, 自动化]
comment: LLM 给的 slug 翻译居然一次过
info: 折腾 2 天终于跑通，开心
---

## 背景

一直想用微信就能发博客，但 GitHub Pages 没有原生支持。

## 怎么做的

写了个 webhook 服务，picoclaw 转发微信消息过来 → 解析 meta → LLM 翻 slug → 推 GitHub。

## 踩的坑

- MiniMax-M3 是推理模型，max_tokens 不够就被截断
- slug 提取要把 think 块剥掉
- Jekyll 用的 date 字段是 UTC，要加时区
