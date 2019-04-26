#coding:utf-8
import getSong,getSongList,sys,os
sys.path.append('../module')
#import dataIn#, getArtists #,dataOut
# import makeCharts

def main():
	#------------------------爬取歌曲信息
	# songUrl = "https://music.163.com/#/song?id=1334596367"#songUrl
	# songInfo = getSong.getSong(songUrl)
	
	#------------------------爬取歌单中的歌曲信息
	# listUrl='https://music.163.com/#/playlist?id=37880978'#songListUrl
	# listInfo = getSongList.getList(listUrl)

	#------------------------爬取用户信息(歌单及个人信息)待完善
	#userUrl = 'https://music.163.com/#/user/home?id=284808512'
	# userInfo = getUser.getUser(userUrl)

	#------------------------爬取多个歌单的Id
	#listUrl = ''

	"""爬取歌手列表中的歌手，通过歌手爬取热门歌曲"""
	# url = 'http://music.163.com/discover/artist/cat?id=1001&initial=-1'
	# getArtists.get_artists(url)

	# dataIn.sqlQuery(songInfo)
	# dataOut.sqlQuery(songInfo)

	# makeCharts.charts()



if __name__ == '__main__':
	main()
	
