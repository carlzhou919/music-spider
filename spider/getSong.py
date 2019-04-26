# coding:utf-8
import requests, json, os, sys
sys.path.append('../module')
import dataIn
global headers
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Origin':'http://music.163.com',
    'Host':'music.163.com',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://music.163.com/'
}
"""headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; NTES_SESS=Fa2uk.YZsGoj59AgD6tRjTXGaJ8_1_4YvGfXUkS7C1NwtMe.tG1Vzr255TXM6yj2mKqTZzqFtoEKQrgewi9ZK60ylIqq5puaG6QIaNQ7EK5MTcRgHLOhqttDHfaI_vsBzB4bibfamzx1.fhlpqZh_FcnXUYQFw5F5KIBUmGJg7xdasvGf_EgfICWV; S_INFO=1476597594|1|0&80##|hourui93; NETEASE_AUTH_SOURCE=space; NETEASE_AUTH_USERNAME=hourui93; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=cbd082d2ce2cffbcd5c085d8bf565a95aee3173ddbbb00bfa270950f93f1d8bb4cb55a56a4049fa8c828373f630c78f4a43d6c3d252c4c44f44b098a9434a7d8fc110670a6e1e9af992c78092936b1e19351435ecff76a181993780035547fa5241a5afb96e8c665182d0d5b911663281967d675ff2658015887a94b3ee1575fa1956a5a%3A1476607977016; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476595468.1476606177.8; __utmb=94650624.20.10.1476606177; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}"""
def getsong(url):
    songId = getsongId(url)
    songNameAndPath = getsongInfo(songId)
    songInfo=[]
    songInfo.append(int(songId))
    songInfo += songNameAndPath
    dataIn.sqlQuery(songInfo)
    # print songInfo
    return songInfo

def getsongId(url):
    songId = url.split('/')[-1].lstrip('song?id=')
    return songId

def getsongInfo(songId):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(songId)
    #R_SO_4_1321385090?limit=20&offset=40,limit是页数,offset是偏移量
    # urlsongName = 'http://music.163.com/api/song/detail/?id='+songId+'&ids=%5B'+songId+'%5D'
    
    nameAndPath = []
    response = requests.get(url,headers=headers)

    dataContent = json.loads(response.text)
    # print type(dataContent)
    name = getsongName(songId)
    makePath = '../song/%s_%s' % (songId,name)
    isExists=os.path.exists(makePath)
    path = '../song/'+songId+'_'+name+'/'+songId+'.txt'
    if not isExists:
        os.mkdir('../song/%s_%s' % (songId,name))
        with open(path,'w', encoding='utf-8') as f:
            f.write(str(dataContent))
        
    nameAndPath.append(name)
    nameAndPath.append(path)
    # print nameAndPath
    # hotcomments = []
    # for hotcommment in dataContent['hotComments']:
    #     item = {
    #         'nicknameid':hotcommment['user']['userId'],
    #         'nickname':hotcommment['user']['nickname'],
    #         'contentid':hotcomment['contentId']
    #         'content':hotcommment['content'],
    #         'likedCount':hotcommment['likedCount'],
    #         'imgurl':hotcommment['user']['avatarUrl']
    #     }
    #     hotcomments.append(item)
    return nameAndPath
def getsongName(songId):
    url = 'http://music.163.com/api/song/detail/?id='+songId+'&ids=%5B'+songId+'%5D'
    response = requests.get(url,headers=headers)
    dataContent = json.loads(response.text)
    return dataContent['songs'][0]['name'].strip().replace('\'',' i') #or a list
    
# print(getsongName('1334596367'))
