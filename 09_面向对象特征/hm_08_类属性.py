class Tool(object):

    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("扳手")
print(Tool.count)

