#迭代器
"""
list=[1,2,3]
for i in iter(list):
    print(i)
x=iter(list)
print(next(x))
"""
#在类中创建迭代器
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
