# 1.输入苹果单价
price_str = input("请输出单价：")

# 2.输入数量
weight_str = input("请输出数量：")

# 3.计算金额
# 1>将价格转换成小数
price = float(price_str)

# 2>将价格转换成小数
weight = float(weight_str)

# 3>计算金额
money = price * weight

print(money)
