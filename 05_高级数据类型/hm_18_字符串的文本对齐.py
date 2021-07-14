# 假设以下内容是从网络中抓取的
# 顺序并且居中对齐打印
poem = ["登鹤雀楼\n",
        "王之涣",
        "白日依山尽\r",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_info in poem:
    # 先使用strip方法去除空白字符
    # 再用center方法居中显示
    print("|%s|" % poem_info.strip().center(10, " "))
