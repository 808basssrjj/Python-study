def sum_num(*args):

    num = 0

    print(args)

    for n in args:
        num += n

    return num


result = sum_num(1, 2, 3)
print(result)
