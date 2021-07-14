name_list = ["张三", "李四", "王五"]


# 1.取值和取索引
print(name_list[0])
print(name_list.index("王五"))

# 2.修改
name_list[1] = "李丽"

# 3.增加
# append在末尾增加数据
name_list.append("王小二")
# insert再指定位置插入
name_list.insert(1, "赵六")
# extend将列表追加到列表中
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)

# 4.删除
# remove可以删除指定数据
name_list.remove("张三")
# pop默认删除最后一个数据
name_list.pop()
# pop可以删除指定元素的索引
name_list.pop(1)
# clear可以清空数据
# name_list.clear()


print(name_list)
