def demo(num, num_list):

    print("函数内部代码")

    # num = num + num
    num += num

    # 列表+= 不是num_list = num_list + num_list
    # 本质实在调用 entend方法
    num_list += num_list
    print(num)
    print(num_list)

    print("代码执行完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
