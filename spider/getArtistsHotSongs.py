#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time, re, csv, getSong
import csv, sys
sys.path.append('../module')
import dataIn


def parse_html_page(html):
    # 使用双引号会出现 Unresolve reference
    # pattern = '<span class="txt"><a href="/song?id=(\d*)"><b title="(.*?)">'
    # 这里是使用lxml解析器进行解析,lxml速度快,文档容错能力强,也能使用html5lib
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('span', 'txt')
    return items


'''
# 这里以获取薛之谦的热门歌曲为例
url = "https://music.163.com/#/artist?id=5781"
html = get_html_src(url)
'''


# 将获得的歌手的热门歌曲id和名字写入csv文件
def write_to_csv(items, artist_name):

    with open("artist_HotSongs.csv", "a", encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["歌手名字", artist_name])

        for item in items:
            writer.writerow([item.a['href'].replace('/song?id=', ''), item.b['title']])
        '''
            # 可视化显示
            print('歌曲id:', item.a['href'].replace('/song?id=', ''))
            song_name = item.b['title']
            print('歌曲名字:', song_name)
        '''
    csvfile.close()


# 获取歌手id和歌手姓名
def read_csv():

    with open("artists_hot_IdAndName.csv", "r") as csvfile:

        reader = csv.reader(csvfile)
        for row in reader:
            artist_id, artist_name = row
            if str(artist_id) is "artist_id":
                continue
            else:
                yield artist_id, artist_name
    # 当程序的控制流程离开with语句块后, 文件将自动关闭


def get_Artists_HotSongs(artist_ids):
    # 可以任意选择浏览器,前提是要配置好相关环境,更多请参考selenium官方文档
    driver = webdriver.Chrome()
    # 避免多次打开浏览器
    # for readcsv in read_csv():
        # artist_id, artist_name = readcsv
    for artist_id in artist_ids:
        print("正在获取id为%s的歌手的热门歌曲" % artist_id)
        url = "https://music.163.com/#/artist?id=" + str(artist_id)
        # print("正在获取{}的热门歌曲...".format(artist_name))
        driver.get(url)
        # 切换成frame
        driver.switch_to_frame("g_iframe")
        # 休眠1秒,等待加载完成!
        # time.sleep(1)
        html = driver.page_source
        items = parse_html_page(html)
        # linkre=re.compile('href=\"(.+?)\"')
        # print(linkre.findall(items[0]))
        linkre=re.compile('href=\"(.+?)\"')

        # artist_HotSongId = linkre.findall(str(items[0]))[0].split('/')[-1].lstrip('song?id=')
        # getSong.getSongInfo(artist_HotSongId)
    
        for n in range(len(items)):
            artist_HotSongId = linkre.findall(str(items[n]))[0].split('/')[-1].lstrip('song?id=')
            try:
                songInfo=[]
                songInfo.append(artist_HotSongId)
                songInfo += getSong.getSongInfo(artist_HotSongId)
                dataIn.sqlQuery(songInfo)
            except OSError as err:
                print("系统错误: {0}".format(err))
                print("id为%s的歌曲爬取失败！" % artist_HotSongId)
                continue    
        print("id为%s的歌手的热门歌曲已获取完成\n" % artist_id)
    # for i in soup.find_all('a'):
    #     print(i)
    # print("{}的热门歌曲获取完成!".format(artist_name))
    # print("开始将{}的热门歌曲写入文件".format(artist_name))
    # write_to_csv(items, artist_name)
    # print("{}的热门歌曲写入到本地成功!".format(artist_name))


# read_csv()