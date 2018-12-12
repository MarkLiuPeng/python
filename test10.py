"""
from collections import Iterable,Iterator    #判断可迭代
print(isinstance({},Iterable),isinstance(10,Iterable))  #迭代对象
test=[x*y for x in  range(10) for y in range(20)]
print(isinstance(test,Iterator))    #迭代器

#import math
__import__ ('math')     #字符模块导入
print(dir('math'))
"""
"""
def example(name):
    print("%s"%name)
    while True:
        role=yield
        print("he is %s and name is %s"%(role,name))

x=example("hzs")
print(x.__next__())
print(x.send("boss"))
x.send("worker")
#内置函数
test=filter(lambda x:x%2==0,[1,2,3,4])
for i in test:
    print(i)
class Myclass():
    def __init__(self,name):
        self.name=name
    def get(self):
        print("value:%s"%self.name)
    def __del__(self):
        self.name
test=Myclass("lp")
print(test)
#封装
class Myclass():
    def __init__(self,name,age):
      #  self.__name=nameI
      #  self.__age=age
        self.set_info(name,age)
    def tell_inio(self):
        print("name:%s age:%s:"%(self.__name,self.__age))
    def  set_info(self,name,age):       #变量封装
        if  not isinstance(name,str):
            raise ValueError("name must is str")
        if not isinstance(age,int):
            raise  ValueError("age must  is int")
        self.__name=name
        self.__age=age

test=Myclass("lp",18)
test.tell_inio()

class Myclass:
    def __salary(self):
        print(int("3000"))
    def __sex(self):
        print("man")
    def display(self):      #方法封装
        self.__salary()
        self.__sex()
test=Myclass()
print(test.display())
class Myclass:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def fun(self,*args,**kwargs):
        print("fun")

    @property
    def Fun(self):
        pass
        return "other object "
        #self.name=name
    @property           #属性装饰
    def FunTow(self):
        return ("object test")

test=Myclass("lp",18)
#test_Two=Myclass()
print(test.__dict__,'\n',Myclass.__dict__)


#类的属性方法评估__dict__
"""
class Myclass(object):
    def __init__(self,num):
        self.num=num
    #def get(self):
     #   return(iter(self.num))
    def __iter__(self):            #迭代创造
        return(iter(self.num))


test=Myclass([1,2,3,4])
for i in test:
    print(i)
