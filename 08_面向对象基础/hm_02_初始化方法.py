class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "Tom"


# 使用类名()创建对象时会自动调用__init__方法
tom = Cat()
print(tom.name)
