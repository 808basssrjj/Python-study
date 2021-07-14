# 定义字符串变量name,  输出我叫小明，请多多关照
name = "小明"
print("我叫%s,请多多关照" % name)

# 定义整形变量student_no, 输出 我的学号是000001
student_no = 1
print("我的学号是%06d" % student_no)

# 定义小数 price、weight、money
# 输出苹果单价9.00元/斤，购买了5.00斤，需支付45.00元
price = 8.5
weight = 5
money = price * weight
print("苹果单价 %.f2 元/斤，购买了 %.f3 斤，需支付 %.f4 元" % (price, weight, money))

# 定义一个小数scale ,输出比例是25%
scale = 0.25
print("比例是 %.2f%%" % (scale * 100))
