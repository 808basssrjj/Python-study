i = 0

while i <= 10:

    # continue 某一条件满足时不执行后续代码
    if i == 3:
        # 使用continue需要确认计数是否修改否则会死循环
        i += 1

        continue

    print(i)

    i += 1
