def example(name):
    print("%s"%name)
    while True:
        role=yield
        print("he is %s and name is %s"%(role,name))

x=example("hzs")
print(x.__next__())
print(x.send("boss"))
x.send("worker")
