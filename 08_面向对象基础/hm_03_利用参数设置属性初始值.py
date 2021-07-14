class Cat:

    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象时会自动调用__init__方法
tom = Cat("Tom")
lazy_cat = Cat("大懒猫")

tom.eat()
lazy_cat.eat()
