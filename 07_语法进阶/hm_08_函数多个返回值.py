def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = 39
    wetness = 40
    print("测量结束")

    # 多个返回值用元组可以省略括号
    # return (temp,wetness)
    return temp, wetness


result = measure()
print(result)

# 如果函数返回的是元组，同时希望单独处理元组中的数据
# 可以使用多个变量接受函数的返回值
# 注意:变量个数应和元组中数据数量一样
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
