#coding:utf-8
import sqlConfig
import MySQLdb
def sqlQuery(hotcomments):
	conn = MySQLdb.connect(host=sqlConfig.DB_HOST,user=sqlConfig.DB_USER,passwd=sqlConfig.DB_PASSWORD,db=sqlConfig.DB_DB,charset=sqlConfig.DB_CHARSET)
	cursor = conn.cursor()
	for n in range(len(hotcomments)):
		sql = "insert into aSongComments(contentId,content,nicknameid,nickname,likedCount) values ('%d','%s','%s','%s','%d')  \
		on duplicate key update contentId='%d',content='%s',nicknameid='',nickname='',liked;"\
		% (hotComments[n]['contentId'],hotcomments[n]['content'],hotcomments[n]['nicknameid'],hotcomments[n]['nickname'],hotcomments[n]['likedCount'])
		cursor.execute(sql)
	sql = "insert into user select nickNameId,nickName from asongcomments on duplicate key update userId = nickNameid,userName=nickname;"
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()
def test():
	print 'hello'
def userIn():
	conn = MySQLdb.connect(host=sqlConfig.DB_HOST,user=sqlConfig.DB_USER,passwd=sqlConfig.DB_PASSWORD,db=sqlConfig.DB_DB,charset=sqlConfig.DB_CHARSET)
	cursor = conn.cursor()

# insert into user values ('132873505','123') on duplicate key update userId = '132873505',userName='123';
# insert into user values ('132873504sda','234') on duplicate key update userId = '132873504sda',userName='123';
# Used to handle primary key conflicts
