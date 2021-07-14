info_tuple = ("张三", 18, 1.75)

# 格式化字符串%后的（）本质时元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
