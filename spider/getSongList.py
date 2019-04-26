#coding:utf-8
import requests, json, os, sys
sys.path.append('../module')
import getSong, dataIn

def getListId(url):
    listId = url.split('/')[-1].lstrip('playlist?id=')
    return listId
def getListInfo(listId):
	url = 'http://music.163.com/api/playlist/detail?id=%s' % listId
	response = requests.get(url,headers=getSong.headers)
	listJson = json.loads(response.text)

	for n in range(len(listJson['result']['tracks'])):
		songInfo = []
		# songName listJson['result']['tracks'][0]['bMusic']['name']
		songId = listJson['result']['tracks'][n]['id']
		songInfo.append(songId)
		songInfo += getSong.getSongInfo(str(songId))
		dataIn.sqlQuery(songInfo)
		
def getList(url):
	listId = getListId(url)
	getListInfo(listId)

