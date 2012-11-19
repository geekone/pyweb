# -*- coding:utf-8

__author__ = 'Administrator'

from pyquery import PyQuery as pq

#
#<span class="w1" columnname="日常祝福" columnid="77">10</span>


url = "http://www.aizhufu.cn/duanxinku/column/77/1.html"

from pyquery import PyQuery as pq

#取总分类
def getCategory():
    list = []
    d = pq(url)
    div_treelist = d('.treelist')
    for div in div_treelist:
        list.append(pq(div).find('h1').html())
    return list;

#取子分类
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

#取条目
def getItem():
    list = []
    d = pq(url)
    li_list = d('.readContent')
    for li in li_list:
        #print pq(li).attr('original-title')
        _title =  pq(li).html()
        list.append(_title)
    return list


if __name__ == '__main__':
    getItem()





