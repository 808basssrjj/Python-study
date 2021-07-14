class Animal:

    def eat(self):
        print("吃。。")

    def drink(self):
        print("喝。。")

    def run(self):
        print("跑。。")

    def sleep(self):
        print("睡。。")


# 字类拥有父类的所有属性和方法
class Dog(Animal):

    def bark(self):
        print("汪汪叫")


dog = Dog()
dog.run()
dog.eat()
dog.drink()
dog.sleep()
dog.bark()
