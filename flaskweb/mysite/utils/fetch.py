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
    list = []
    d = pq(url)
    li_treelist = d('.treelist ul li')
    for li in li_treelist:
        _name =  pq(li).find('a').html()
        _subid =  pq(li).find('a').attr('columnid')
        _list = [_name,_subid]
        list.append(_list)
    return list


if __name__ == '__main__':
#    list = getCategory()
#    print list
     list =  getSubCategory()
     for ls in list:
         print ls[0],ls[1]





