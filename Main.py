import urllib3 as ul
import urllib
import requests
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

class getPaperMsg(object):
    def __init__(self):
        pass

if __name__=='__main__':
    # 管理世界
    main_url = 'http://glsj.cbpt.cnki.net/WKB2/'
    web_url = main_url + 'WebPublication/wkTextContent.aspx?colType=4&yt={year}&st={season}'
    response = requests.get(web_url.format(year='2019', season='05'))
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    paper = soup.find_all("ul", class_="column_contbox_zxlist")

    li = []
    for i in range(len(paper)):
        title = paper[i].find_all("a")[0].text
        author = paper[i].find_all("samp")[0].text
        abstract = paper[i].find_all("p")[0].text
        download_url = main_url + paper[i].find_all("a")[-1].get('href').split('../')[1]
        key_url = main_url + paper[i].find_all("a")[1].get('href').split('../')[1]

        response2 = requests.get(key_url)
        content2 = response2.text
        soup2 = BeautifulSoup(content2, 'html.parser')
        paper2 = soup2.find_all("p")
        key_word = paper2[2].text.split('关键词(KeyWords)：')[1].strip()
        li.append([title, author, abstract, key_word, download_url])




'''
    import pymysql

    # 打开数据库连接
    db = pymysql.connect("10.100.203.223", "hadoop", "Jtbi@123")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("show databases")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()

    print(data)

    # 关闭数据库连接
    db.close()
'''
