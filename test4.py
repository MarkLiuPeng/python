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


#另一个继承类
class speak():
    title=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.title=t
    def speak(self):
        print("我叫:%s正在学习%s语言"%(self.name,self.title))
#多继类方法
class sample(speak,Student):
    a=''
    def __init__(self,n,a,s,S,t):
        Student.__init__(self,n,a,s,S)
        speak.__init__(self,n,t)


x=sample("lp",18,"man",100,"python")
#x=Student("lp",18,"man",100)
x.speak()


'''
'''
class Myclass:
    def __init__(self): #构造方法
        self.data=[]

x=Myclass()
'''
'''
class Parent:
    def test(self):
        print("Parent Class")
class Son(Parent):
    def test(self):
        print("Son Class")
x=Son()
x.test()
super(Son, x).test()        #重写

class Myclass:
    __ssum=0  #私有变量
    psum=0      #公开变量
    def sum(self):
        self.__ssum+=1
        self.psum+=1
        print(self.__ssum)

test=Myclass()
test.sum()
test.sum()

print(test.__ssum)
print(test.psum)
'''

class Myclass:
    def __init__(self,name,url):
        self.name=name
        self.__url=url
    def who(self):
        print("name:",self.name)
        print("url:",self.__url)
    def __get(self):  #私有方法
        print("s")
    def get(self):     #公有方法
        print("p")
        self.__get()

test=Myclass("baidu","www.baidu.com")
test.who()
test.get()
test.__get()
