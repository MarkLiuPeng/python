#异常处理
#raise NameError('error')
#模块
'''
import os
str=os.name
if str=='nt':
    print("you system is windows")
elif str== 'unix':
    print("you system is linux")
else:
    print("you system os other")
    '''
'''
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age

x=MyClass("lp",18)
print(x.name,x.age)
'''
"""
    i=1
    def test(self):
        return("test Function")
x=MyClass()
print(x.i)
print(x.test());
"""
'''
class Test:
    def prt(example):
        print(example)
        print(example.__class__)
t=Test()
t.prt()
'''
#父类
class  People:
    name=''         #类基本属性
    age=0
    sex=''
    __height=0      #私有属性
    def __init__(self,n,a,s):
        self.name=n
        self.age=a
        self.sex=s
        #self.__height=h
    def speak(self):
        print("%s说：我%d岁和性别%s."%(self.name,self.age,self.sex))
#子类
class Student(People):
    score=0
    def __init__(self,n,a,s,S):
        People.__init__(self,n,a,s)   #调用父类的构造函数
        self.score=S
    def speak(self):            #调用父类的方法
        print("%s说：我%d岁和性别%s我的分数是%d."%(self.name,self.age,self.sex,self.score))


x=Student("lp",18,"man",100)
x.speak()

'''
class Myclass:
    def __init__(self): #构造方法
        self.data=[]

x=Myclass()
'''
