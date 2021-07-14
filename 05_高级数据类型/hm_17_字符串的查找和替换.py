hello_str = "hello python"

# 1.判断是否以指定字符串开头
print(hello_str.startswith("hello"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("python"))

# 3.查找指定字符串,返回索引
print(hello_str.find("llo"))
# index字符串不存在会报错 find会返回-1
print(hello_str.find("abc"))

# 4.替换字符串
# 执行后会返回新的字符串不会修改原来字符串
print(hello_str.replace("python", "world"))
print(hello_str)
