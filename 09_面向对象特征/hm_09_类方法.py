class Tool(object):

    # 类属性
    count = 0

    # 类方法
    @classmethod
    def show_tools_count(cls):
        print("工具的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
Tool.show_tools_count()
