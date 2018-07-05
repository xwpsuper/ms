# # -*- coding: UTF-8 -*-

# import time
# import requests
# from lxml import etree


# def qpN(N, list1):
#     LL = []
#     if len(list1) >= N:
#         for i in range(len(list1)):
#             if (i+1) % N == 0:
#                 l = list1[:N]
#                 if l in LL:
#                     pass
#                 else:
#                     LL.append(l)
#                 for i in l:
#                     if i in list1:
#                         list1.remove(i)
#             else:
#                 pass
#     return LL

# def parser_cplssj(url):
#     r = requests.get(url)
#     r = r.content.decode('utf-8')
#     html = etree.HTML(r)
#     # result = etree.tostring(html) #输出是编码有问题

#     res = html.xpath(r'//tbody/tr/td')

#     count = 0
#     count1 = 0
#     L=[]
#     for i in res:
#         if count1 < 8:
#             L.append(i.text)
#         count1 += 1
#         try:
#             if '2018-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2017-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2016-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2015-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2014-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2013-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2012-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2011-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2010-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2009-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2008-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             elif '2007-' in i.text:
#                 L.append(i.text)
#                 count = 8
#             else:
#                 if count > 0:
#                     # print('count====', count)
#                     L.append(i.text)
#                     count -= 1
#         except:
#             pass
#     print(L)
#     LLL = qpN(9, L)
#     with open('cplssj.txt', 'a') as f:
#         for i in LLL:
#             f.write(str(i) + ',' + '\n')
# for i in range(1, 87):  #查看网页数据一共有多少页，这里有86页

#     url = 'http://www.lottery.gov.cn/historykj/history_'+ str(i) +'.jspx?_ltype=dlt'
#     try:
#         parser_cplssj(url)
#         time.sleep(0.01)
#     except:
#         print(url)

# -*- coding: UTF-8 -*-

import time
import requests
from lxml import etree


def qpN(N, list1):
    LL = []
    if len(list1) >= N:
        for i in range(len(list1)):
            if (i+1) % N == 0:
                l = list1[:N]
                if l in LL:
                    pass
                else:
                    LL.append(l)
                for i in l:
                    if i in list1:
                        list1.remove(i)
            else:
                pass
    return LL

def parser_cplssj(url):
    r = requests.get(url)
    r = r.content.decode('utf-8')
    html = etree.HTML(r)
    # result = etree.tostring(html) #输出是编码有问题

    res = html.xpath(r'//tbody/tr/td')

    count = 0
    count1 = 0
    L=[]
    for i in res:
        if count1 < 8:
            L.append(i.text)
        count1 += 1
        try:
            if '2018-' in i.text:
                L.append(i.text)
                count = 8
            elif '2017-' in i.text:
                L.append(i.text)
                count = 8
            elif '2016-' in i.text:
                L.append(i.text)
                count = 8
            elif '2015-' in i.text:
                L.append(i.text)
                count = 8
            elif '2014-' in i.text:
                L.append(i.text)
                count = 8
            elif '2013-' in i.text:
                L.append(i.text)
                count = 8
            elif '2012-' in i.text:
                L.append(i.text)
                count = 8
            elif '2011-' in i.text:
                L.append(i.text)
                count = 8
            elif '2010-' in i.text:
                L.append(i.text)
                count = 8
            elif '2009-' in i.text:
                L.append(i.text)
                count = 8
            elif '2008-' in i.text:
                L.append(i.text)
                count = 8
            elif '2007-' in i.text:
                L.append(i.text)
                count = 8
            else:
                if count > 0:
                    # print('count====', count)
                    L.append(i.text)
                    count -= 1
        except:
            pass
    LLL = qpN(9, L)
    return(LLL)
LLLL = []
for i in range(1, 87):  #查看网页数据一共有多少页，这里有86页

    url = 'http://www.lottery.gov.cn/historykj/history_'+ str(i) +'.jspx?_ltype=dlt'
    try:
        LL = parser_cplssj(url)
        LLLL += LL
        time.sleep(0.01)
    except:
        print(url)
    print(i)
print(LLLL)