#计算方法
def add(x,y):
    """加函数"""
    return(x+y)
def even(x,y):
    """减函数"""
    return(x-y)
def pows(x,y):
    """积函数"""
    reutrn(x*y)
def losr(x,y):
    """商函数"""
    return(x/y)

#运算符选择
print("select your char:")
print("1>加")
print("2>减")
print("3>积")
print("4>商")
#测试数值
num1=int(input("输入你的第一个数字:"))
num2=int(input("输入你的第二个数字:"))
choice=input("选择你的运算(1/2/3/4)")

if choice=='1':
    print(num1,'+',num2,'=',add(num1,num2))
elif choice=='2':
    print(num1,'-',num2,'=',even(num1,num2))
elif choice=='3':
    print(num1,'*',num2,'=',pows(num1,num2))
elif choice=='4':
    print(num1,'/',num2,'=',losr(num1,num2))
else:
    print("运算符有误")
