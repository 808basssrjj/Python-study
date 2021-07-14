class MusicPlay(object):

    def __new__(cls, *args, **kwargs):

        # 创建对象时，会自动调用new方法
        print("创建对象，分配空间")

        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlay()
print(player)
