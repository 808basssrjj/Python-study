name_list = ["张三", "李四", "王五", "张三"]

# len函数统计元素的总数
list_length = len(name_list)
print("列表中包含%d个数据" % list_length)

# count方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了%d次" % count)
