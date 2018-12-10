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

'''
class Myclass:
    def Fun(self,*args):
        pass    #占位

test=Myclass()
test.Fun()
