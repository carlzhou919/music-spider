#coding:utf-8
import sqlConfig
# import pymysql #python2:MySQLdb
def sqlQuery(songInfo):
	conn = pymysql.connect(host=sqlConfig.DB_HOST,user=sqlConfig.DB_USER,passwd=sqlConfig.DB_PASSWORD,db=sqlConfig.DB_DB,charset=sqlConfig.DB_CHARSET)
	cursor = conn.cursor()
	for n in range(len(hotcomments)):
		sql = "insert into song values ('%s','%s','%s')" % (songInfo[0],songInfo[1],songInfo[2])
		cursor.execute(sql)
	sql = "insert into user select nickNameId,nickName from asongcomments on duplicate key update userId = nickNameid,userName=nickname;"
	try:
		sql = "insert into song values ('%s','%s','%s') on duplicate key update songId = '%s',songName='%s',songPath='%s';" % (songInfo[0],songInfo[1],songInfo[2],songInfo[0],songInfo[1],songInfo[2])
		cursor.execute(sql)
		conn.commit()
	except Exception:
		print("数据插入出错，错误信息：%s "+Exception % songInfo[0])
	# print("插入数据成功")
	
	cursor.close()
	conn.close()
def test():
	print(hello)
def userIn():
	conn = MySQLdb.connect(host=sqlConfig.DB_HOST,user=sqlConfig.DB_USER,passwd=sqlConfig.DB_PASSWORD,db=sqlConfig.DB_DB,charset=sqlConfig.DB_CHARSET)
	cursor = conn.cursor()
	sql=""
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()
