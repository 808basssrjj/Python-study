def input_pwd():

    # 1.提示输入密码
    pwd = input("请输入密码:")
    # 2.判断密码长度是否>=8
    if len(pwd) >= 8:
        return pwd

    # 3.如果<8主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象-可以使用错误信息字符串作为参数
    ex = Exception("密码长度小于8")
    # 2> 主动抛出异常
    raise ex


try:
    input_pwd()
except Exception as result:
    print(result)
