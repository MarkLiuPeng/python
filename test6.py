'''
i=[1,2,3]
j=[1,2,3,4,5]
def IjFun():
    #i,j=0
    if len(i)<len(j):
        #if i%j==0:
            print(i+j)
def  otherFun():
    for x in len(i):
        for y in len(j):
            print(x,y)

#char='python'
#print(repr(char),str(char))
#格式输出

for  x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end='')
    print(repr(x*x*x).rjust(4))
    print('{0:d} {1:2d} {2:3d}'.format(x,x*x,x*x*x))
tb={"lp":"man","wp":"women","ye":"man"}
for name,sex in tb.items():
    print('{0:10} =》 {1:10}'.format(name,sex))
#file=open('1.txt','r')
#file.close()

#file.write("python")
#file.read()
#自动关闭文件对象
import json #json模块
with open('1.txt','r+') as file:
    securt=json.load(file)  #解码文件
    json.dump(securt,file)  #编码文件
    #data=securt.read()
#print(file.closed)
#print(data)

#异常处理
while True:
    try:        #未发生异常
        x=int(input("Input Number:"))
        break
    except ValueError:  #异常触发,跳转try继续执行
        print("error,again")
import sys
try:
    f=open('1.txt')
    s=f.readline()
    l=int(s.strip())
except OSError as err:
    print("OSError {0}".format(err))
except ValueError:
    print("none")
except:
    print("sys.exec_info()[0]")
    raise

for i in  sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print("can't open",arg)
    else:   #
        print(arg,'has',len(f.readlines ()),'lines')
        f.close()

def Faild():
    x=1/0
try:
    Faild()
except ZeroDivisionError as err:
    print(err)
try:
    raise NameError("you have error")   #触发异常
except  NameError:
    print("none")
    raise
class Error():
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return(repr(self.value))

try:
    raise Error(2*2)
except  Error as err:
    print(err.value)
#raise Error("none")
try:
    raise KeyboardInterrupt
finally:
    print("bye")

def Fun(i,j):
    try:
        result=i/j
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is:",result)
    finally:        #清理行为,无论是否被触发异常，都会被执行
        print("none")

Fun(4,2)
Fun(4,0)
Fun("4","2")
'''
#预定义清理行为
with open('1.txt') as file:
    #print(file.closed)
    for content in file:
        print(content)
