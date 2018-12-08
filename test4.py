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
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age

x=MyClass("lp",18)
print(x.name,x.age)
"""
    i=1
    def test(self):
        return("test Function")
x=MyClass()
print(x.i)
print(x.test());
"""
