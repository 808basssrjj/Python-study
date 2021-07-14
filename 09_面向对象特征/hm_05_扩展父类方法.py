class Animal:

    def eat(self):
        print("吃。。")

    def drink(self):
        print("喝。。")

    def run(self):
        print("跑。。")

    def sleep(self):
        print("睡。。")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("飞")

    def bark(self):
        # 1.针对子类特有需求，编写代码
        print("喵喵喵")

        # 2.使用super()，调用原本父类方法
        super().bark()

        # 3.增加其他字类代码
        print("afafa")


xtq = XiaoTianQuan()

xtq.bark()
