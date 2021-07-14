class Women:
    def __init__(self, name):

        self.name = name

        # 定义私有属性
        self.__age = 18

    # 定义私有方法
    def __secret(self):
        # 私有属性可以再内部访问
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 私有属性不可以在外部访问
print(xiaofang._Women__age)
# 私有方法不可以在外部直接访问
xiaofang._Women__secret()
