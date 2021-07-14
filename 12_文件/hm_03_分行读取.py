# 打开
file = open("readme.txt", encoding="UTF-8")

# 读取
while True:
    text = file.readline()

    if not text:
        break
    print(text)
# 关闭
file.close()
