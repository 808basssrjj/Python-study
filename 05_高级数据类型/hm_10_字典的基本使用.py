xiaoming_dic = {"name": "小明"}

# 1.取值
print(xiaoming_dic["name"])

# 2.增加/修改
# 如果key不存在会增加键值对
xiaoming_dic["age"] = 18
# 如果key存在会修改value
xiaoming_dic["name"] = "小小明"

# 3.删除
xiaoming_dic.pop("name")


print(xiaoming_dic)
