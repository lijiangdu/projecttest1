# !/usr/bin/env python
# -*- coding:utf-8 -*-


# def fun1(*a):
#     i=j=k=0
#     while i<3:
#         j=0
#         while j<3:
#             k=3-i-j
#             if (i!=j) and (i!=k):
#                 print(a[i],a[j],a[k])
#             j+=1
#         i+=1
# a=["first","second","third"]
# fun1(*a)
# def sub_combination(left,right):
#     if len(left)>0:
#         for item in left:
#             new_right = right+ [item]
#             new_left = [x for x in left if x!=item]
#             sub_combination(new_left,new_right)
#     else:
#         print(right)
# def combination(l):
#     return sub_combination(l,[])
# combination(["first","second","third"])
# 袋子问题
# def solve(a,wei,num):
#     if num <= 0:
#         return False
#     for s in a :
#         if s<=wei:
#             a = [x for x in a if x != s]
#             if wei == s:
#                 return True
#             else:
#                 if solve(a, wei-s, num-1):
#                     return True
# if(solve([1,2,3],3,3)):
#     print("True")
# else:
#     print("False")
# if(solve([10,12,13],35,3)):
#     print("True")
# else:
#     print("False")
# if(solve([10,12,13],12,3)):
#     print("True")
# else:
#     print("False")
# 汉诺塔问题
# hanio=[[1,2,3,4,5,6,7,8,9,10],[],[]]
# numtotal=0
# def move(from_,to,num_):
#     if num_==1:
#         x=hanio[from_].pop(0)
#         hanio[to].insert(0,x)
#         global numtotal
#         numtotal+=1
#         print(u"将第%d片从第%d根柱子移动到第%d根柱子"%(x,from_+1,to+1))
#         print(u"移动后的状态为%s" % hanio)
#         print("次数为%d"%numtotal)
#     if num_>1:
#         val=3-from_-to
#         move(from_,val,num_-1)
#         move(from_,to,1)
#         move(val,to,num_-1)
# move(0,2,10)
# 模块
# child.hello()
# 文件
fd = open("in.dat","a")
fd.write("你算什么东西")
fd.write("what are you?")
fd.close()
fd = open("in.dat","r")
for line in fd:
    print(line+"\n")
fd.close()
# fd = open("D:/111/111.dat","r",encoding="utf-8")
# for line in fd:
#     print(line)
# fd.close()
# 正则表达式
import re;
# def vaild_email(addr):
#     result=re.match(r"^[a-zA-Z0-9]+@[a-z0-9]+\.[a-z0-9]*$",addr)
#     if result is None:
#         print(r"[%s] is not a vaild email" %addr)
#     else:
#         print(r"[%s] is a vaild email" % addr)
# vaild_email("2378353779@qq.com")
# print("dawd\ndwadwf")
# print(r"dawd\ndwadwf")
# aaa=re.match(r"\d\d\dSS(Ss)*","999SSSs")
# if aaa is not None:
#     print(aaa)
# input_str="dwa5457gggg5seg2gd222"
# input_str2="d6666wa5457gggg5seg2gd222"
# result=re.search(r"\d+",input_str)
# print(input_str2[result.start():result.end()])
#时间库
# import time
# a= time.time()
# print(a)
# b=time.gmtime(a)
# print("%d年%d月%d日%d时%d分%d秒%d周%d天%d夏令时"%b)
# print("%d年%d月%d日%d时%d分%d秒%d周%d天%d夏令时"%(b.tm_year,b.tm_mon,b.tm_mday,b.tm_hour,b.tm_min,b.tm_sec,b.tm_wday,b.tm_yday,b.tm_isdst))
# c=time.mktime(b)
# print(c+8*60*60)
#日期库
# import datetime
# a=datetime.datetime.today()
# print(a.year,a.month,a.day,a.hour,a.minute,a.second)
# b=a.weekday()
# print(b)
# c=a.ctime()
# print(c)
#二叉树库
# import binarytree
# root = binarytree.Node(1.5)
# root.left=binarytree.Node(2.3)
# root.right=binarytree.Node(3.4)
# print(root)
# print(root.preorder)
#二叉树结点只能是float或者int类型
# 随机数random
import random
# num1=0
# num2=0
# totalnum=10000
# while totalnum>0:
#     rannum=random.random()
#     if rannum<=0.1:
#         num1+=1
#     if rannum<=0.6 and rannum>0.1:
#         num2+=1
#     totalnum-=1
# print(u"0-0.1有 %s 个，占 %f"%(num1,num1/10000.0))
# print(u"0.1-0.6有 %s 个，占 %f"%(num2,num2/10000.0))
rannum=random.randint(2,4)
print(rannum)
# a=[1,2,3,4,5,6]
# print(random.choice(a))
# random.shuffle(a)
# print(a)
# 洗牌
# def cards():
#     ret = []
#     for i in range(1, 14):
#         ret.append((i, u"方块"))
#         ret.append((i, u"梅花"))
#         ret.append((i, u"红心"))
#         ret.append((i, u"黑桃"))
#     ret.append((14, u"大王"))
#     ret.append((14, u"小王"))
#     return ret
# card=cards()
# random.shuffle(card)
# sss=0
# for cards in card :
#     if cards[0]==14 and sss<17:
#         print(cards[1])
#         sss += 1
#     elif cards[0]!=14 and sss<17:
#         print(cards[1],cards[0])
#         sss += 1
# print(sss)
# 捕获异常
# try:
#     s=10/0
#     print("right")
# except:
#     print("wrong")
# def div(a,b):
#     try:
#         c=b/a
#         return c
#     except ZeroDivisionError as ex_obj:
#         print(u"被0除的异常，错误为：%s" %ex_obj)
#     except Exception as  e:
#         print(u"其他异常，错误为：%s" %e)
# div(0,"10")
# div(0,10)
# def except_demo(a,b):
#     if b==0:
#         raise Exception('666')
# try:
#     except_demo(12, 0)
# except Exception as e:
#     print("message is %s"%e)
# 类
#self.对象名   这种是针对这个类的一个对象起作用
#类名.对象名    这种是针对这一种类的所有对象起作用，相当于static
#对象名        在这个类中的这个函数中创建的一个对象，只在当前函数中起作用
# class InstanceNum:
#     instance = 0
#
#     def __init__(self, age):
#         self.instance = self.instance + 1
#         self.age = age
#         print("Init :%s %s" % (self.instance, self.age))
#
#     def __del__(self):
#         self.instance = self.instance - 1
#         print("del :%s %s" % (self.instance, self.age))
#
#
# inst1 = InstanceNum(1)
# del inst1
# inst2 = InstanceNum(2)
# inst3 = InstanceNum(3)
# del inst2
# inst4 = InstanceNum(4)
# del inst4
# del inst3     #self.属性名只在当前实例有效果
#
# class InstanceNum:
#     instance = 0
#
#     def __init__(self, age):
#         InstanceNum.instance = InstanceNum.instance + 1
#         InstanceNum.age = age
#         print("Init :%s %s" % (InstanceNum.instance, InstanceNum.age))
#
#     def __del__(self):
#         InstanceNum.instance = InstanceNum.instance - 1
#         print("del :%s %s" % (InstanceNum.instance, InstanceNum.age))
#
#
# inst1 = InstanceNum(1)
# del inst1
# inst2 = InstanceNum(2)
# inst3 = InstanceNum(3)
# del inst2
# inst4 = InstanceNum(4)
# del inst4
# del inst3       #类名.属性名，相当于全局变量，对该类中的对象都有效
#将类外部的函数变为类内部的函数
# def obj_method():
#     print("inside obj_method")
#     print("obj.name = [%s]" %obj_method.__self__.name)
# class Student:
#     version = "1.0"
#     author = "python.cn"
#     def __init__(self):
#         self.name = "傻鸟"
#     def update_method(self,val):
#         self.new_method = val
#         val.__self__=self
# student_a = Student()
# if hasattr(student_a,"new_method"):
#     print("yes")
# else:
#     print("no")
# if hasattr(student_a,'update_method'):
#     print("yes")
# else:
#     print("no")
# student_a.update_method(obj_method)
# if hasattr(student_a,"new_method"):
#     print("yes")
# else:
#     print("no")
# if hasattr(student_a,'update_method'):
#     print("yes")
# else:
#     print("no")
# student_a.new_method()
#静态方法
#静态方法跟非静态方法一样都能改变该类对象的值
#对象方法可以改变该实例中该对象的值
#类方法是直接对类中的对象进行操作
# class Student:
#     highest_score = None
#     lowest_score = None
#     def __init__(self):
#         self.name = ""
#     # @staticmethod
#     # def the_most_score():
#     #     Student.lowest_score-=1
#     #     Student.highest_score+=1
#     #     print("the highest score is %s the lowest score is %s" %(Student.highest_score , Student.lowest_score))
#     def the_most_score(self):
#         self.lowest_score-=1
#         self.highest_score+=1
#         print("the highest score is %s the lowest score is %s" %(self.highest_score , self.lowest_score))
#         # Student.lowest_score-=1
#         # Student.highest_score+=1
#         # print("the highest score is %s the lowest score is %s" %(Student.highest_score , Student.lowest_score))
#     def setscore(self, score):
#         if Student.highest_score==None or score > Student.highest_score:
#             Student.highest_score = score
#         if Student.lowest_score==None or score < Student.lowest_score:
#             Student.lowest_score = score
#     @ classmethod
#     def high_score2(cls):
#         print(cls.highest_score,cls.lowest_score)
# student_a = Student()
# student_a.setscore(50)
# student_a.setscore(51)
# student_a.setscore(49)
# student_a.setscore(48)
# student_a.setscore(60)
# student_a.the_most_score()
# print(Student.highest_score,student_a.lowest_score)
# student_b = Student()
# print(student_b.highest_score,student_b.lowest_score)
# student_a.high_score2()
#只读属性
#只读属性的函数在调用的时候不需要加上括号，其不能被修改，@proporty只能用来修饰函数
#使用__setarr__()函数，能够指定某些对象只读,在__init__初始化函数中就已经开始起作用
# class Student:
#     version = "1.0"
#     author = "god"
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self._age = age
#     # @property
#     def age(self):
#         print("调用了这个函数")
#         return self._age
#     def test(self):
#         print("你要怎么搞？")
#         return 1
#     def __setattr__(self, key, value):
#         if key=='age':
#             msg='{}.{} is READ ONLY'.format(type(self).__name__,key)
#             raise AttributeError(msg)
#         else:
#             self.__dict__[key] = value
# student_a = Student("alex","女",18)
# # print(student_a.age)
# # student_a.age
# student_a.age =21
# print(student_a.age)
# student_a.version="1.1"
# print(student_a.version)
#类的安全检查
#使用property()函数来定义age属性
# class Student:
#     version = "1.0"
#     author = "god"
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self._age = age
#     # @property
#     def get_age(self):
#         print("调用了age函数")
#         return self._age
#     def test(self):
#         print("你要怎么搞？")
#         return 1
#     def set_age(self,new_age):
#         if new_age>40 or new_age<14:
#             print("Invalid age value")
#             return None
#         self._age=new_age
#         return new_age
#     age = property(get_age,set_age)
# student_a = Student("alex","女",18)
# print(student_a.age)
# student_a.age=21
# print(student_a.age)
#用age属性设置函数来定义
# class Student:
#     version = "1.0"
#     author = "god"
#     def __init__(self,name,gender,age):
#         self.name = name
#         self.gender = gender
#         self._age = age
#     @property
#     def age(self):
#         print("调用了age函数")
#         return self._age
#     def test(self):
#         print("你要怎么搞？")
#         return 1
#     @age.setter
#     def age(self,new_age):
#         if new_age>40 or new_age<14:
#             print("Invalid age value")
#             # return self._age
#         else:
#             self._age=new_age
#     @age.getter
#     def age(self):
#         return self._age
# student_a = Student("alex","女",18)
# print(student_a.age)
# student_a.age=21
# print(student_a.age)
# student_a.age=50
# print(student_a.age)
#多重继承
# class Birds:
#     """鸟类"""
#     def lay_egg(self):
#         print("下蛋中")
#     def die(self):
#         print("鸟类死亡")
# class CanSwim:
#     """水生类"""
#     def swim(self):
#         print("游泳中")
#     def die(self):
#         print("水生类死亡")
# #继承的夫类如果属性出现重复，以引用括号内第一个父类的属性为准
# class Penguin(Birds,CanSwim):
#     """企鹅"""
#     def __init__(self):
#         self.swim()
#         self.lay_egg()
#         self.die()
#         print("看小孩中")
# penguin = Penguin()
#多重继承按照“从左至右，广度优先”的方式去查找属性
# class P1():
#     def foo(self):
#         print('p1-foo')
#     def bar(self):
#         print('p1-bar')
#
#
# class P2():
#     def foo(self):
#         print('p2-foo')
#
#     def bar(self):
#         print('p2-bar')
#
#
# class C1(P1,P2):
#     pass
#
# class C2(P1,P2):
#     def bar(self):
#         print('C2-bar')
#
#
# class D(C1,C2):
#     pass
#
#
# if __name__ =='__main__':
#     d=D()
#     d.foo()
#     d.bar()
#复杂多重继承
#super()采用的是mro里面的直接父类
# class A(object):
#     def __init__(self):
#         print ('init A...')
#     def t1(self):
#         print('At1')
#     def t2(self):
#         print('At2')
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print ('init B...')
#     # def t1(self):
#     #     print('Bt1')
#     def t2(self):
#         print('Bt2')
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print ('init C...')
#     def t1(self):
#         print('Ct1')
#     def t2(self):
#         print('Ct2')
#
# class D(B,C):
#     def __init__(self):
#         super().__init__()
#         # C.__init__(self)
#         # C.__init__(self)
#         print ('init D...')
# d = D()
# d.t1()
# print(B.mro())
# print(D.mro())
#https://www.cnblogs.com/superxuezhazha/p/5737967.html
#https://www.cnblogs.com/mingaixin/archive/2013/01/31/2887043.html
#https://zhuanlan.zhihu.com/p/106963767
# import nltk
# nltk.download();
# import torch
# print (torch.__version__)
# print(torch.cuda.is_available())
# print(torch.cuda.device_count())
import hpelm
# import numpy as np
# X = np.array([[1, 1], [1, 0], [1, 0], [0, 1], [0, 1], [1, 1]])
# f=X.shape[1];
# print(f)
# import pydicom
# import matplotlib.pyplot as plt
# ds = pydicom.dcmread("E:/project/data/t1/Test_Sets/CT/3/DICOM_anon/i0000,0000b.dcm")
# plt.figure(figsize=(10, 10))
# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()