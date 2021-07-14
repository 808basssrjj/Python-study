def say_hello():
    print("你好我是sayhello")


# 如果直接执行模块，输出__main__
if __name__ == "__main__":
    print(__name__)

    print("小明开发的模块")

    say_hello()
