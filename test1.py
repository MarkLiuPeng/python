#字符
"""
str="panjing"
print(str[3:5]);
#列表方法
list=['walk','bike']
del list[1]
print(list*100)
#元组方法
tuple=('salary','age','name')
print(len(tuple))
#字典方法
dict={'name':'lp','sex':'man','age':18}
print(dict)
#集合方法
x={'firset','second','third','four','five','third'}
print(x)
y=set('firset')
print(y)
#列表推导式
z={example  for example  in 'abclpabc' if example not in 'abc'}
print(z)
"""
x,y=0,1
while y<100:
    print(y,end=',')
    x,y=y,x+y
