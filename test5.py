#模块
'''
 #-*- coding:encoding -*-
#编码
'''

'''
import re
print('python lanuange'.replace('python','shell'))

list=['python','java','shell']
for i in  range(len(list)):
    print(i,list[i])
#for i in list:
    #print(i,len(i))
#lists=lambda list:list.append(lanuange)
#print(lists)
    #print(i,list[i])
for x in range(2,10):
    for y in range(2,x):
        if x % y==0:
            print(x,'equals',y,'*',x//y)
            break
        else:
            print(x,'not is')

for x in range(2,10):
    if x%2==0:
        print('a odd number:',x)
        continue
    else:
        print('a j number:',x)
class Myclass:
    def Fun(self,*args):
        pass    #占位

test=Myclass()
test.Fun()
def Fun(a,list=[]):
    list.append(a)
    return list

for i in range(10):
    print(Fun(i))
def Fun():
    """Document"""
    pass    #文档字符串
print(Fun.__doc__)
                    #函数注解
def Fun(age:18,num:int='test') -> "Funtion example":
    print("",Fun.__annotations__)
    print("",age,num)x`
Fun("test")
list=[]
lists=[input()]
list.extend(list)
print(list)
list=[1,2,3]
list.append(4)  #堆栈列表
print(list)
print(list.pop(),list.pop(),list)      #释放列表
from collections import deque
list=deque(['python','java','shell'])
list.append('c')
list.append('html')
list.popleft()
list.popleft()
print(list)
list=['a','b',1]
del list[1:2]
print(list)
x=set('abcde')
y=set('aadg')
print(x | y ,x ^ y)
    #序列化字典
#print(dict([('name','lp'),('sex','man'),('age',18)]))
#dict={x:x*2 for x in range(10)}
print(dict(name='lp',sex='man',age=18))
'''
import test6
print(test6.__name__)
test6.IjFun()
