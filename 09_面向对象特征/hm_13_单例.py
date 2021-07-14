class MusicPlay(object):

    # 记录第一个创建对象的引用
    instance = None
    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:

            # 2.调用父类方法为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance


player1 = MusicPlay()
print(player1)

player2 = MusicPlay()
print(player2)
