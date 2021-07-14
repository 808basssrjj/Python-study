def test(num):
    print("在函数内部%d的内存地址是%d" % (num, id(num)))


# 定义一个数字变量
a = 10
print("a变量保存数据的内存地址是%d" % id(a))

test(a)
