name_list = ["张三", "李四", "王五"]

# 使用del删除数据
# 日常中使用列表提供的方法
del name_list[1]

# del关键字本质时将一个变量从内存中删除
name = "小明"
del name
print(name)

print(name_list)
