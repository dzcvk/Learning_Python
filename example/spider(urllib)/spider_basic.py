import urllib.request
import re

word = urllib.request.quote('科技')
url = 'http://sug.so.360.cn/suggest/word?callback=suggest_so&encodein=utf-8&encodeout=utf-8&word='

headers = {
			"GET":url+word,
			"HOST":'sug.so.360.cn',
			'referer':'http://www.so.com'
		}



req = urllib.request.Request(url+word)
for item in headers:
	req.add_header(item,headers[item])

html = urllib.request.urlopen(req).read()
html=html.decode('utf-8')
strSq= re.findall("\"(.*?)\"",html)
#print(html.decode('utf-8'))
for item in strSq:
	print(item)