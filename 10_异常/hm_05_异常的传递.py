def demo1():
    return int(input("请输入一个整数:"))


def demo2():
    return demo1()


# 利用异常的传递再主程序捕获异常
try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知异常%s" % result)
