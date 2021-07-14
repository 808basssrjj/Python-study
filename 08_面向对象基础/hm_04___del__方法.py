class Cat:

    def __init__(self, new_name):

        self.name = new_name
        print("%s被创建了" % self.name)

    # 对象销毁时最后调用的方法
    def __del__(self):
        print("%s被销毁了" % self.name)


tom = Cat("Tom")
print(tom.name)
