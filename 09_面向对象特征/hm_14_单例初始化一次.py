class MusicPlay(object):

    # 记录第一个创建对象的引用
    instance = None

    # 记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:

            # 2.调用父类方法为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1. 判断是否执行过初始化方法
        if MusicPlay.init_flag:
            return

        # 2. 如果没有执行，再执行初始化方法
        print("初始化播放器")

        # 3. 修改类属性标记
        MusicPlay.init_flag = True


player1 = MusicPlay()
print(player1)

player2 = MusicPlay()
print(player2)
