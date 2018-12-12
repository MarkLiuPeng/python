"""
import  random
Age=random.randrange(10) #随机生成0-10中的1个数字
count=0
i=0
#for i in range(10):
while count<10:
    if i<3:
    #if i < 2:
        Test_age=int(input("Please Inout Your Age"))
        if Age == Test_age:
            print("your age  right")
            break
        elif Age>Test_age:
            print("your age is big")
        else:
            print("your are right!")
        i+=1
       # count=count+1
    #elif:
    else:
        single=int(input("Please Input Your choice"))
        if single=='Y':
            i=0
        #    count=0
        else:
            print("bye")
            break
    count+=1
    #else:
     #   print("many")
str='pythonpythonooo'
count=0
i=0
while(str.find('o'))>0:
    count+=1
    index=str.find('o')
    i=index+1
    str=str[i:]
print(count)
#print(1<2)      #布尔
import copy
list=['python','shell',['变量','语句','类','函数'],'c']    #嵌套列表
print(list)
list_Tow=list.copy()        #浅拷贝    外层列表参与软连接共享，内层不参与
print(list_Tow)
list[2][1]='数据类型'
print(list,'\n',list_Tow,'\n',id(list[2]),'\n',id(list_Tow[2]),'\n',id(list),'\n',id(list_Tow))
list_Tow.append("递归")
print(list,list_Tow)
list_four=copy.deepcopy(list)   #深拷贝        内存独立，包括内外层
print('old:','\n',list_four,'\n',list)
del list_four[2][3]
print('new:','\n',list_four,'\n',list)
s1={"python","shell","c","php"}
s2={"html","css","javascriipt"}
print(s1.difference(s2))
import sys
print(sys.getdefaultencoding())#字符编码
"""

"""
import time
for i in range(50):
    sys.stdout.write("#")
    sys.stdout.flush()  #调用同步刷写到磁盘
    time.sleep(0.2)

    #if i%2==0:
      #  time.sleep(0.5)

str="python"
str
def digui(n):
    if n<100:
        print(n)
        return(digui(n+1))      #调用函数自身递归
digui(10)
def Gaojie(x,y,f):
    print(f(x)+f(y))      #高阶函数
Gaojie('l','p',str)

list=['python','shell','javascript']
print(id(list))
def Fun(x):
    print(id(x))
    print(id(Fun))
print(Fun)
"""

#装饰器
"""
import time
def timmer(func):       #外层函数
    def warpper(x):    #内层装饰
        print(x)
        start_time=time.time()
        func()
        stop_time=time.time()
        print("This function run time is %s"%(stop_time-start_time))
        #return(timmer)
    return(warpper)

@timmer             #修饰器
def test():
    time.sleep(3)
    print("test1")
test()
"""
def explain(func):
    def warrper(*args,**kwargs):
        #不带参数的修饰器
        print("----begin----")
        test=func(*args,**kwargs)
        #func()
        #print("----end------")
        print("%s%s"%(args,kwargs))
        return(test)
    return(warrper)
@explain
def test(x,y,z):
    print("python")
    #print("talk")
    return(2)
test('b','a',z='c')


