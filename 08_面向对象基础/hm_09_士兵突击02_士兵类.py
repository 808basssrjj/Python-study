class Gun:

    def __init__(self, model):

        # 枪的型号
        self.model = model
        # 子弹数量
        self.buttet_count = 0

    def add_buttet(self, count):

        self.buttet_count += count

    def shoot(self,):

        # 判断子弹数量
        if self.buttet_count <= 0:
            print("%s 没有子弹了" % self.model)
            return

        # 发射子弹
        self.buttet_count -= 1

        # 提示信息
        print("[%s] 哒哒哒...[%d]" % (self.model, self.buttet_count))


class Soldier:

    def __init__(self, name):
        self.name = name
        # 不知道定义社么初始值，可以设置为None
        self.gun = None


# 创建枪对象
ak47 = Gun("Ak47")
ak47.add_buttet(50)
ak47.shoot()
# 创建许三多对象
xvsanduo = Soldier("许三多")
xvsanduo.gun = ak47
print(xvsanduo)
