import urllib3 as ul
import urllib
import requests
from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
if __name__=='__main__':
    baiduwenku_url = 'https://wenku.baidu.com/view/e93a4307941ea76e59fa04c7.html'

    content = requests.get(baiduwenku_url).text

    soup = BeautifulSoup(content, 'html.parser')
    paper = soup.find_all("div", class_="ie-fix")
    print(paper)

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