# 计算1+2+..num
def sun_numbers(num):

    # 1.递归出口
    if num == 1:
        return 1

    temp = sun_numbers(num-1)
    return num + temp


print(sun_numbers(100))
