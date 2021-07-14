import card_tools

while True:

    # 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择希望执行的操作:")
    print("你选择的操作是 [%s] " % action_str)

    # 1 2 3针对名片操作
    if action_str in ["1", "2", "3"]:
        # 1新增名片
        if action_str == "1":
            card_tools.new_card()
        # 2修改名片
        elif action_str == "2":
            card_tools.show_all()
        # 3查询名片
        else:
            card_tools.search_card()

    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片系统】")
        break
        # 使用pass关键字，表示一个占位符，保证程序代码结构完整
        # pass

    # 其他输入提示输入错误
    else:
        print("你输入的不正确，请重新选择")
