row = 1

while row <= 5:

    col = 1

    # 再加一个循环负责每一列的星星
    while col <= row:

        print("*", end="")

        col += 1

    print("")

    row += 1
