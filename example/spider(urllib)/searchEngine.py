import urllib.request
from bs4 import BeautifulSoup

key=input('type in key')
#observe the pattern of search url
search_url='http://www.baidu.com/s?wd=key&rsv_bp=0&rsv_spt=3&rsv_n=2&inputT=6391'
# search your keyword
req=urllib.request.urlopen(search_url.replace('key',key))
result=[]  #store result
for count in range(10):#search for 10 pages
        html=req.read()
        soup=BeautifulSoup(html)
        result+=[i.string for i in soup('a',{'onmousedown':True})]
        next_page='http://www.baidu.com/'+soup('a',{'href':True,'class':'n'})[0]['href'] # search for the next page
        req=urllib.request.urlopen(next_page)
f=open(r'result.txt','w')
for i in result:
        f.write(i+'\n')
f.close()

input('enter')
