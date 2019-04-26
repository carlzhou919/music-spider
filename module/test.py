# coding:utf-8
import requests, json, os, sys
sys.path.append('../module')
sys.path.append('../spider')
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Origin':'http://music.163.com',
    'Host':'music.163.com',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://music.163.com/'
}
def getSongInfo(songId):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(songId)
    #R_SO_4_1321385090?limit=20&offset=40,limit是页数,offset是偏移量
    # urlSongName = 'http://music.163.com/api/song/detail/?id='+songId+'&ids=%5B'+songId+'%5D'
    
    # nameAndPath = []
    response = requests.get(url,headers=headers)

    dataContent = json.loads(response.text)
    hotcomments = []
    for hotcomment in dataContent['hotComments']:
        item = {
            'nicknameid':hotcomment['user']['userId'],
            'nickname':hotcomment['user']['nickname'],
            # 'contentid':hotcomment['contentId'],
            'content':hotcomment['content'],
            'likedCount':hotcomment['likedCount']
            # 'imgurl':hotcomment['user']['avatarUrl']
        }
        hotcomments.append(item)
    return hotcomments

def charts(hotcomments):
    content_list = [content['content'] for content in hotcomments]
    nickname = [content['nickname'] for content in hotcomments]
    liked_count = [content['likedCount'] for content in hotcomments]

    bar = Bar("热评中点赞数示例图")
    bar.add( "点赞数",nickname, liked_count, is_stack=True,mark_line=["min", "max"],mark_point=["average"])
    bar.render()

    content_text = " ".join(content_list)
    wordcloud = WordCloud(font_path=r"C:\simhei.ttf",max_words=200).generate(content_text)
    plt.figure()
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()
songId="543607345"
charts(getSongInfo(songId))