# -*- coding: utf-8 -*-

import re
import urllib,urllib2
import os

#urllib:
#urllib2: The urllib2 module defines functions and classes which help in opening
#URLs (mostly HTTP) in a complex world — basic and digest authentication,
#redirections, cookies and more.


def translate(text):
    '''模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果 '''
    #text 输入要翻译的英文句子
    text_1=text
    #'langpair':'en'|'zh-CN'从英语到简体中文
    #values={'hl':'zh-CN','ie':'UTF-8','text':text_1,'langpair':"'en'|'zh-CN'"}
    values={'hl':'en','ie':'UTF-8','text':text_1,'langpair':"'zh-CN'|'en'"}
    url='http://translate.google.cn/translate_t'
    data = urllib.urlencode(values)
    req = urllib2.Request(url,data)
    #模拟一个浏览器
    browser='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
    req.add_header('User-Agent',browser)
    #向谷歌翻译发送请求
    response = urllib2.urlopen(req)
    #读取返回页面
    html=response.read()
    #从返回页面中过滤出翻译后的文本
    #使用正则表达式匹配
    #翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
    #.*? non-greedy or minimal fashion
    #(?<=...)Matches if the current position in the string is preceded
    #by a match for ... that ends at the current position
    p=re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m=p.search(html)
    text_2=m.group(0).strip(';')
    text_2=text_2.strip("'")
    text_2=text_2.strip('"')
    text_2=text_2.replace('"', '')
    text_2=text_2.replace("'", "")
    text_2=text_2.replace("%", "%")
    return text_2

path = '/Users/iclaud/Documents/shinemoon.github.io/_posts'
for file in os.listdir(path):
	if os.path.isfile(os.path.join(path,file))==True:
		if file.find('%')>0:
			#print 
			realfilename = urllib.unquote(file).replace('.html','').replace("《","-").replace("》","-").replace("「","").replace("」", "").replace("——", "-").replace("--", "-").replace("（","").replace("）", "").replace("？", "").replace("：", "").replace("，","").replace("[","").replace("]","")
			m = re.match(r'(\d\d\d\d-\d\d-\d\d-)(.*)', realfilename)
			cdate = m.groups()[0]
			cname = m.groups()[1]
			print cname
			transname = translate(cname).replace(" " , "-")
			cleanp = re.compile(r"-+")
			#remove duplicated -
			transname = re.sub(cleanp, "-" , transname)
			#remove final -
			cleanp = re.compile(r"-$")
			transname = re.sub(cleanp, "" , transname)
			#clean some symbol
			cleanp = re.compile(r"[,\.]")
			transname = re.sub(cleanp, "" , transname)
			cleanp = re.compile(r'&#39')
			transname = re.sub(cleanp, "" , transname)

			finalname = cdate + transname.replace(" " , "")
			#print finalname

			#改名字

			newname=finalname + ".html"
			try:
				os.rename(os.path.join(path,file),os.path.join(path,newname))
			except:
				print 'some os issue'
			print file,'ok'
