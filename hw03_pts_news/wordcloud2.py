# In[1]
import jieba
import wordcloud
import matplotlib.pyplot as plt

import os

current_directory = os.getcwd()
print("當前工作目錄路徑：", current_directory)
file_path = "C:/Users/jilly/PL/PL_TAHRD/hw03_pts_news/ptscontent2.txt"


# In[2]
# 讀取文本文件
with open (file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 使用 jieba 進行中文分詞
seg_list = jieba.cut(text, cut_all=False)
text = " ".join(seg_list)

# 創建文字雲
wc = wordcloud.WordCloud(width=800, height=400, background_color='white', font_path='MSYH.TTC')
wc.generate(text)

# 顯示文字雲圖片
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()


