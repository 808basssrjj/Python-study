# 定义结果的变量
result = 0

# 定义计数器
i = 0

# 开始循环
while i <= 100:

    # 判断i是否偶数
    if i % 2 == 0:

        print(i)

        result += i

    i += 1

print("结果 = %d" % result)
