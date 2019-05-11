import jieba
import wordcloud
txt="一溜串汉字"
w.wordCloud.WordCloud(width=1000,\
                      font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")
#中文需要先分词并组成空格分隔字符串
