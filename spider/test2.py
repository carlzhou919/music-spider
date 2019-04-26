#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: zhiying
URL: www.zhouzying.cn
Date: 2018-9-9
Description: 爬取网易云音乐歌手热门歌曲
"""

# from selenium import webdriver
import re
from bs4 import BeautifulSoup
def main():
	str = 'that\'s a apple'
	# print(str)\
	# linkre=re.compile('href=\"(.+?)\"')
	# print(linkre.findall(str))
	print(str.replace('\'',' i'))

if __name__ == "__main__":
	main()