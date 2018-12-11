#! -*- encoding:utf-8 -*-   #字符编码
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
"""

list=['python','shell',['变量','语句','类','函数'],'c']    #嵌套列表
print(list)

