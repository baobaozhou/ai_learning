
# coding: utf-8

# In[ ]:


from urllib.request import urlopen
html=urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)


# In[ ]:


import re
res=re.findall(r"<title>(.+?)</title>",html)
print(res[0])


# In[ ]:


import re
res=re.findall(r'<p>(.+?)</p>',html,flags=re.DOTALL) #res为一个列表，用于审查源码中有多少个p对
print(res[0])


# In[ ]:


import re
res=re.findall(r'a href="(.+?)"',html)#（）里边的为匹配的内容
for lines in res:
    print(lines)


# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)
soup=BeautifulSoup(html,features='lxml')#lxml为解析器
res=soup.find_all('a')#a为标签，hreef为属性
print(res)
for lines in res:
    print(lines['href'])


# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://morvanzhou.github.io/static/scraping/list.html').read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
res=soup.find_all('li',{'class':'month'})
for lines in res:
    print(lines.get_text())
res1=soup.find('ul',{'class':'jan'})
print(res1)
res2=res1.find_all('li')
for line in res2:
    print(line.get_text())


# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('https://morvanzhou.github.io/static/scraping/table.html').read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
res1=soup.find_all('a',{'href':re.compile('.+?')})
for line in res1:
     print('链接为：'+ line['href'])
res=soup.find_all('img',{'src':re.compile('.+?\.jpg')})
for lines in res:
    print(lines['src'])


# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
n=0
base_url = 'https://baike.baidu.com'
his=['/item/%E8%9C%98%E8%9B%9B/8135707']
while n<100:
    url=base_url+his[n]
    html=urlopen(url).read().decode('utf-8')
    soup=BeautifulSoup(html,features='lxml')
    print(soup.find('h1').get_text()+'链接为：'+url)
    res=soup.find_all('a',{'target':'_blank','href':re.compile('/item/(%.{2})+$')})
    if len(res)!=0:
        his.append(random.sample(res,1)[0]['href'])
    else:
        his.pop()
    n=n+1


# In[ ]:


import requests
import re
#模仿登录
payload = {'username': 'zhouhuiquan', 'password': 'password'}
url="http://pythonscraping.com/pages/cookies/welcome.php"#
session=requests.Session()
r=session.post(url,data=payload)
# print(r.cookies.get_dict())
res=session.get(url)
print(res.text)


# In[ ]:


data = {'firstname': 'huiquan', 'lastname': 'zhou'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)
# file = {'uploadFile': open('./image.png', 'rb')}
# r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
# print(r.text)

