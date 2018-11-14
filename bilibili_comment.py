# -*-coding:utf8-*-

from lxml import etree
import requests
import sys
import re
import collections
import io
import pandas as pd

reload(sys)

sys.setdefaultencoding('utf-8')

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}


danmu_dict = {}

def spider(av):
    url = 'http://bilibili.com/video/av' + str(av)
    print(url)
    html = requests.get(url, headers=head)
    selector = etree.HTML(html.text)
    content = selector.xpath("//html")
    for each in content:
        title = each.xpath('//*[@id="viewbox_report"]/h1/span')
        if title:
            print(title[0].text)
            cid_html_1 = each.xpath('//*[@id="link2"]/@value')
            if cid_html_1:
                cid_html = cid_html_1[0]
                cids = re.findall(r'cid=.+&page', cid_html)
                cid = cids[0].replace("cid=", "").replace("&page", "")
                comment_url = 'http://comment.bilibili.com/' + str(cid) + '.xml'
                print(comment_url)
                comment_text = requests.get(comment_url, headers=head)
                comment_selector = etree.HTML(comment_text.content)
                comment_content = comment_selector.xpath('//i')
                for comment_each in comment_content:
                    comments = comment_each.xpath('//d/@p')
                    if comments:
                        num = 0
                        time_list = []
                        for comment in comments:
                            #print(comment)
                            # print type(comment.split(',')[0])
                            # #print str(comment.strip(','))
                            time_list.append(comment.split(',')[0])
                            dict_key = int(comment.split(',')[0].split('.')[0])
                            if danmu_dict.has_key(dict_key):
                                danmu_dict[dict_key] = danmu_dict[dict_key] + 1
                            else:
                                danmu_dict[dict_key] = 1
                            # if danmu_dict.has_key(comment.split(',')[0])
                            # danmu_dict[]
                            num+=1
                            #f.writelines(comment.decode("utf-8") + '\n')
                    # print num
                    # print time_list
            else:
                print('cid not found!')
        else:
            print('video not found!')



if __name__ == '__main__':
    av = "22395161"
    #f = io.open(av + '.txt', 'w', encoding='utf-8')
    spider(av)
    #print danmu_dict
    list_1 = []
    list_2 = []
    for key in danmu_dict:
        list_1.append(key)
        list_2.append(danmu_dict[key])
    dataframe = pd.DataFrame({"time":list_1,"data":list_2})
    # print dataframe
    dataframe.to_csv("test.csv",index=False,sep=',')

