row = 1

while row <= 9:

    col = 1

    # 再加一个循环负责每一列的星星
    while col <= row:

        # print("*", end="")
        print("%d * %d = %-2d" % (col, row, col * row), end="\t")

        col += 1

    print("")

    row += 1
