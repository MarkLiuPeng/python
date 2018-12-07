#迭代器
"""
list=[1,2,3]
for i in iter(list):
    print(i)
x=iter(list)
print(next(x))
"""
#在类中创建迭代器
"""
class MyClass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <= 10:    #规定迭代的次数
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration #触发结束
newclass=MyClass()
test=iter(newclass)
for i in test:
    print(i)
"""
#生成器
''''
import sys
def Function(n):
    x,y,count=0,1,0
    while True:
        if(count>n):
            return
        yield x
        x,y=x,x+y
        count+=1
example=Function(20)

while True:
    try:
        print(next(example),end=' ')
    except StopIteration:
        sys.exit()
'''

#函数
"""
def Function(length,width):
    print(length*width)
    #return length*width
Function(10,20)
"""
'''
def Function(name, sex='man'):  #参
    print("name:",name)
    print("sex:",sex)
    return

            #不可变长度参数
Function('lp')
def Function(args,*tuple):
    print(args)
    print(tuple)
Function(1,2,3)
def Function(args,**dict):
    print(args)
    print(dict)
Function(1,x=1,y=2)
def Function(x,*,y):
    print(x+y)
    return x+y
Function(1,y=3)
#匿名函数
sum=lambda x,y:x+y
print("sum:",sum(1,2))
#变量
def PFunction():
    num=1
    def Function():
        nonlocal num
        #    global num
        print(num)
        num=10
    Function()
    print(num)
PFunction()
#列表推导式
var_new=[j*i for i in range(10) for j in range(20)]
print(var_new)
login={"name":"lp","sex":"man","age":18}
for k,v in login.items():
    print(k,v)
'''
#模块
''''
import sys
for i  in sys.argv:
    print(i)
print("directory path:",sys.path)
from mode import Max,Min
Max(1,2)
Min(1,2)
'''
if __name__=="__main__":
    print("ourself
else:
    print("other")
