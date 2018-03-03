
import requests

from bs4 import BeautifulSoup

import re


# 1. 下载https://en.wikipedia.org/wiki/Machine_translation 页面的内容并保存为mt.html需要编写代码来下载页面。
session = requests.session()
response = session.get(url="https://en.wikipedia.org/wiki/Machine_translation")
with open('mt.html','wb') as f:
    f.write(response.content)


# 2、统计mt.html中<p>标签内下所有单词以及数目并存储到mt_word.txt中

# 解析页面，拿到所有的p标签中的文本
soup = BeautifulSoup(response.text,features="lxml")
tag2 = soup.find_all(name='p')
list_p = []
for i in tag2:
    list_p.append(i.get_text())

# 将所有的文本合并成一个字符串
str_p = ' '.join(list_p)
# print(str_p)
word_set = set()
for word in str_p.split():
    # print(word);
    word = word.strip(',.()""/; ')
    word_set.add(word)
# word_dict = {}
word_list = []
for word in word_set:
    if word == '':
        continue
    # word_dict[word] = str_p.count(word)
    dict2 = {word:str_p.count(word)}
    word_list.append(dict2)

# 将单词按照数目反序排列，然后写入文件
print(list(word_list[0].values())[0]);
blist = sorted(word_list,key = lambda x:list(x.values())[0],reverse =True)
with open('mt_word.txt','w') as f:
    for item in blist:
        for k,v in item.items():
            line = k + '\t' + str(v) + '\n'
            f.write(line)
            
# 3、提取出mt.html中所有的年份信息（比如说页面中的1629, 1951这些的四位数字就是年份）存储到mt_year.txt中
year = re.compile(r'\d{4}')
years_list = re.findall(year,response.text)
years_list = sorted(list(set(years_list)))
with open('mt_year.txt','w') as f:
    for year in years_list:
        line = year + '\n'
        f.write(line)