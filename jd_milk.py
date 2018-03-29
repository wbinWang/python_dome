#!/usr/bin/python3
#统计京东牛奶销量
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import json
import collections
def get_goodsID():
    goodsId = input("请输入产品ID")
    return goodsId

def get_comments():
    url = 'https://item.jd.com/2922989.html'
    req = requests.get(url)
    req.encoding = 'gbk'
    bsHtml = BeautifulSoup(req.text , "html.parser")
    # print(bsHtml)
    tab_cons = bsHtml.find_all('div',class_="tab-con")
    print(tab_cons[-1])
    # comment_items = bsHtml.find_all('div',class_='user-column')
    # print(comment_items)

def wb_json_comment():
    ctimes = []
    for i in range(0,100):
        url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv253583&productId=2922989&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1' % i
        req = requests.get(url)
        req.encoding = "gbk"
        resp = req.text
        resp = resp.replace("fetchJSON_comment98vv253583(","")
        resp = resp.replace(");","")
        # print(resp)
        jsonText = json.loads(resp)
        # print(jsonText)
        for one in jsonText['comments']:
            #评论内容
            content = one['content']
            #评论时间
            cTime = one['creationTime']
            cTime = cTime.replace("-","")
            cTime = cTime.split(" ")[0]
            ctimes.append(cTime)
    ctimes.sort()
    print(ctimes)
    print(collections.Counter(ctimes))



if __name__ == "__main__":
    wb_json_comment()

