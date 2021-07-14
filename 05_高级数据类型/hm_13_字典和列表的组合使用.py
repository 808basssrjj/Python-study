# 将多个字段放在一个列表中，再进行遍历
card_list = [
    {"name": "张三",
     "qq": "123456",
     "number": "10086"},
    {"name": "李四",
     "qq": "654321",
     "number": "110"}
]

for card_info in card_list:
    print(card_info)
