class Dog(object):

    # 定义静态方法
    @staticmethod
    def run():
        # 不访问对象属性、方法也不访问类属性和方法
        print("小狗爱跑")


# 类名.方法 不需要创建对象
Dog.run()
