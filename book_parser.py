import requests
from lxml import etree

r = requests.get('https://www.hkslg.net/5/5068/index.html')
r.encoding = 'gb2312'
r.text

html = etree.HTML(r.text)
result = html.xpath('//td//a/@href')
L = []
for i in result:
    if i[0] == '/':
        L.append(i)

url = 'https://www.hkslg.net'
for i in L:
    url1 = url + i
    rb = requests.get(url1)
    rb.encoding = 'gb2312'
    rb.text

    html1 = etree.HTML(rb.text)
    result1 = html1.xpath('//p')
    with open('zzgs.txt', 'a', encoding='utf-8') as f:
        f.write(result1[0].xpath('string(.)').strip() + '\n')   #多行文本内容
        