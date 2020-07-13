# -*- coding: utf-8 -*-

"""
 @ Author:  annie.hu
 @ CreateTime:   2020/7/13 12:45 PM
 @ Usage:它将 function 映射于 iterable 中的每一项，并返回一个新的迭代器。

"""

# 例1 如下map函数实现每个元素加1：map(function, iterable, …)

mylist=[1,3,3,4,1]
result=map(lambda x:x+1,mylist)
