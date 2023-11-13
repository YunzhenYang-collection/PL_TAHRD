# In[1]
import jieba
import jieba.analyse

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#import wordcloud 
from wordcloud import WordCloud, ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude

# In[2]
#讀入資料
txtfile = "4-1_ptscontent2_vs.txt" # 剛才下載存的文字檔 

Text = open(txtfile,"r",encoding="utf-8").read()

#設定jieba繁體中文字典
file_path = 'dict.txt'
jieba.set_dictionary(file_path)

#進行斷詞
seg_list = jieba.cut(Text, cut_all=True) # 預設模式。cut_all=True- 全切模式 切的很碎

#傳回list結構
seg_list = jieba.lcut(Text, cut_all=True)

# In[3]
#正規表達式刪除贅字
#import re

#抽取關鍵詞
'''
計算TF-IDF分數，依重要性排列詞頻(Term Frequency, TF)-逆向檔案頻率(Inverse Document Frequency, IDF)
計算之，其中分別是[是指說計算各個分詞在文章中出現的頻率]與[是指說計算分詞在各個文章中出現的頻率]
TF-IDF即為將TF分數與IDF分數相乘後的值進行比較，若分數越高，則該字詞重要性越大
'''
jieba.analyse.extract_tags(Text, topK=10, withWeight=False, allowPOS=())

#利用分析出來的結果，利運pandas做字數頻率統計
import pandas as pd
def count_segment_freq(seg_list):
  seg_df = pd.DataFrame(seg_list,columns=['seg'])
  seg_df['count'] = 1
  sef_freq = seg_df.groupby('seg')['count'].sum().sort_values(ascending=False)
  sef_freq = pd.DataFrame(sef_freq)
  return sef_freq

sef_freq = count_segment_freq(seg_list)
sef_freq.head()

#設定中文字型
#font_path = 'TaipeiSansTCBeta-Regular.ttf' # 
font_path = 'NotoSansTC-Regular.otf' # 字型路徑

seg_list=' '.join(seg_list) #做成list

# 遮罩圖片
mask_color = np.array(Image.open('parrot-by-jose-mari-gimenez2.jpg'))
mask_color = mask_color[::3, ::3]
mask_image = mask_color.copy()
mask_image[mask_image.sum(axis=2) == 0] = 255

# Edge detection 鸚鵡圖片邊緣偵測
edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i]/255., 2) for i in range(3)], axis=0)
mask_image[edges > .08] = 255



#文字雲繪製參數設定
wc = WordCloud(
  background_color='black',        #   背景顏色
  max_words=500,                   #   最大分詞數量
  mask=mask_image,                       #   背景圖片
  max_font_size=None,              #   顯示字體的最大值
  font_path=font_path,             #   若為中文則需引入中文字型(.TTF)
  random_state=None,               #   隨機碼生成各分詞顏色
  prefer_horizontal=0.9)           #   調整分詞中水平和垂直的比例

# 生成詞雲
wc.generate(seg_list)

#利用wordcloud內的ImageColorGenerator()上色
image_colors = ImageColorGenerator(mask_color)
wc.recolor(color_func=image_colors) #依照原圖上色

#重要詞頻結果儲存
file_name='2Etoday_content_clean_pure_cloud-2_result.txt'
#file_name='pts_ptscontent2_clean_cloud-1_result.txt'
with open(file_name, 'w',encoding='utf-8') as f: 
    for key, value in wc.words_.items(): 
        f.write('%s:%s\n' % (key, value))

#繪製成圖形

plt.imshow(wc,interpolation="bilinear")
plt.axis('off') #關掉座標
plt.show() #展示圖片


