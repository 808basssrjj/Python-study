# 打开
file_read = open("readme.txt", encoding="UTF-8")
file_write = open("readme2.txt", "w", encoding="UTF-8")

# 读、写
text = file_read.read()
file_write.write(text)

# 关闭
file_read.close()
file_write.close()
