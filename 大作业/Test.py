#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/19 21:24
# @Author  : Aries
# @Site    : 
# @File    : Test.py
# @Software: PyCharm
from multiprocessing import Pool
import requests
import json
import os
def get_page(url):
    print("<进程%s> get %s"%(os.getpid(),url))
    response=requests.get(url)
    # if response.status_code==200:
    return {'url':url,'text':response.text}

def pasrse_page(res):
    print("<进程%s>parse %s"%(os.getpid(),res['url']))
    parse_res="url:<%s> size:[%s]\n"%(res["url"],len(res["text"]))
    with open("db.txt",'a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    p=Pool(3)
    res_l=[]
    for url in urls:
        res=p.apply_async(get_page,args=(url,))
        res_l.append(res)
    p.close()
    p.join()

    for res in res_l:
       print(res,res.get(),'----------')
