# -*- coding: utf-8 -*- 
# 引入需要使用到的库
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
import re
import platform
from lxml import etree
from datetime import datetime

main_page_url ="https://piyao.sina.cn/"
chrome_driver_path = ""

if platform.system()=='Windows':
    chrome_driver_path = "chromedriver.exe"
elif platform.system()=='Linux' or platform.system()=='Darwin':
    chrome_driver_path = "./chromedriver"
else:
    print('Unknown System Type. quit...')

chrome_options = Options()
#chrome-options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver_path)
driver.get(main_page_url)
time.sleep(3)

#count=0

for i in range(0,24):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    i += 1
    time.sleep(4)

oHtml=driver.page_source
html=etree.HTML(oHtml)
driver.quit()

count=0


sort_tct=[]


while True:
    count+=1
    time=html.xpath('/html/body/div[1]/div[1]/div[3]/div[1] /div[%s] /div[1]/text()'%str(count))
    titles=html.xpath('/html/body/div[1]/div[1]/div[3]/div[1] /div[%s]/ul/li/a/div[1] /div[1]/text()'%str(count))
    comments=html.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[%s]/ul/li/a/div[1]/div[2]/div[2]/text()'%str(count))
    
    if time[0][7]=='4':
        break

    comment_int=[int(i) for i in comments]#把评论数变成int型

    tct=zip(time*len(titles),titles,comment_int)
    tct=[i for i in tct]
    sort_tct.extend(tct)

    
    

high_point=sorted(sort_tct,key=lambda x: x[2],reverse=True)
print("2019年5月至今捉谣记热评十大谣言:")
for x in high_point[:10]:
    print("时间:",x[0],'\t',"标题:",x[1],'\t',"评论数:",x[2])


