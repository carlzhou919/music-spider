#coding:utf-8
import json
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

def getSongCommentInfo(songPath):
	with open(songPath,'r',encoding='utf-8') as f:
		print(json.loads(f.read().replace('\'','\"')))



# songPath="../song/108485_AlwaysOnline/108485.txt"
# getSongCommentInfo(songPath)

