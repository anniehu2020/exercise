# -*- coding: utf-8 -*-

"""
 @ Author:  annie.hu
 @ CreateTime:   2020/7/13 12:31 PM
 @ Usage:调用 filter_self，筛选出满足指定身高的学生

"""


# filter(function, iterable)　　过滤器，过滤掉不满足函数 function 的元素，重新返回一个新的迭代器。
# 这个函数大概等价于下面自定义函数 filter_self：


def filter_self(function,iterable):
    return iter([item for item in iterable if function(item)])


# 调用 filter_self，筛选出满足指定身高的学生。其条件是，男生身高超过 1.75，女生身高超过 1.65。

class Student():
    def __init__(self,name,sex,height):
        self.name=name
        self.sex=sex
        self.height=height


def height_condition(stu):
    if stu.sex=="male":
        return stu.height>1.75
    else:
        return stu.height>1.65


students=[Student('xiaoming','male',1.74),
          Student('xiaohong', 'female', 1.68)]

students_satisfy = filter_self(height_condition,students)
for stu in students_satisfy:
    print(stu.name)
