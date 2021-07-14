class Person:

    def __init__(self, name, weight):
        # selt.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是 %s 体重是%.2f" % (self.name, self.weight)

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1

    def run(self):
        print("%s 爱跑步，跑步减肥" % self.name)
        self.weight -= 0.5


xiaoming = Person("小明", 75.0)
xiaoming.eat()
xiaoming.run()
print(xiaoming)

xiaomei = Person("小美", 45.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
