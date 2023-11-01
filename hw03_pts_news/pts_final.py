#程式碼參考網址 https://gist.github.com/wutienyang/6bf22fdb1f7e704ae7b7fd280f16beda
import requests
from bs4 import BeautifulSoup
import os #刪檔案的套件
# 如果有先前的檔案，先砍掉原本檔案，再重新寫一個
try:
    #open('4_title_vs.txt')
    os.remove('4_title.txt')
except:
    print("Didn't open")
cat=[4] #新聞類別設定

end_page=300 #設定抓的頁數(網頁中下一頁的符號)
for category in cat:
    urls = [] #網頁網址的串列變數
    for page in range(1, end_page+1):
        title = []                   
        u = "https://news.pts.org.tw/category/" + str(category)+"?"+"page="+str(page)  #找到頁數的規律是ttps://news.pts.org.tw/category/cat?page=n 
          
        global soup #將soup設為全域變數，以供抓內文使用
        res = requests.get(u) #利用.get抓取原始碼
        soup = BeautifulSoup(res.content, "lxml") #設定bs4的變數 (可能要先 pip install lxml)
        soup = soup.find_all("h2")#, class_="idle-news-title"，找到原始碼當中有<h2>的地方
        
        for a in soup: #利用bs抓取標題字串
            p = a.a.string  #p是標題字串變數
            title.append(p) 
            urls.append(a.a['href'])
        #開始寫檔        
        with open(str(category)+"_titles.txt", "a", encoding='UTF-8') as f:
            i=1;
            f.write('-----category-'+str(category)+', '+str(page)+'--------'+"\n")#分頁標籤
            for t in title:
                f. write(str(i)+'.'+t+"\n")
                i+=1            
    #print(urls)
# In[]
#抓取內文     
    allcontent = [] #全部內文            
    for u in urls:
        content = []#目前抓的內文
        res = requests.get(u) #利用.get向網頁要原始碼
        soup = BeautifulSoup(res.content, "lxml") #設定bs變數
        try:
            soup = soup.find("div", class_="post-article text-align-left") #內文藏在: <div class="post-article text-align-left" 
            for a in soup.find_all("p"): #文字寫在<p>，找到所有的p              
                p = a.string
                if p != None:
                    p = p.split('/')  # 分割文字
                    if len(p) > 1:
                        content.append(p[1])
                    else:
                        content.append(p[0])
            allcontent.append(content) #將目前抓到的內文放進全部內文中
        except:
            pass
        
    with open(str(category)+"-1_ptscontent2_vs.txt", "a",  encoding='UTF-8') as f:#將內文寫檔
         i=1;
         for c in allcontent:
             if len(c) > 0:
                ss = ""
                for p in c:
                    ss += p+'' #內文內容
                #f.write("link-"+str(i)+":\n"+ss+"\n") #分頁符號
                f.write("\n"+ss+"\n") #純文字
                i+=1