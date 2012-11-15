# -*- coding:utf-8

__author__ = 'Administrator'

from pyquery import PyQuery as pq

url = "http://www.aizhufu.cn/duanxinku/column/77/1.html"

from pyquery import PyQuery as pq


def getCategory():
    list = []
    d = pq(url)
    div_treelist = d('.treelist')
    for div in div_treelist:
        list.append(pq(div).find('h1').html())
    return list;


def getSubCategory():
    pass


if __name__ == '__main__':
    list = getCategory()
    print list





