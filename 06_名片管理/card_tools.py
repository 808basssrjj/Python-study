# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("[1] 新增名片")
    print("[2] 显示全部")
    print("[3] 查询名片")
    print("[0] 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("使用功能:新增名片")

    # 1.提示用户输入信息
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    email_str = input("请输入邮箱:")

    # 2.使用用户输入的信息建立一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将字典添加到列表中
    card_list.append(card_dict)
    # 4.提示新建成功
    print("添加的%s成功" % name_str)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("使用功能:显示全部")

    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("没有名片记录，先增加名片")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)

    # 遍历名片列表
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("使用功能:搜索名片")

    # 1.提示用户输入姓名
    find_name = input("请输入搜索的名字")

    # 2.遍历名片信息，查询要搜索的姓名，如果没有找到提示用户
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到的名片记录执行修改和删除操作
            deal_card(card_dict)

            break
    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片信息

       :param find_dict:查找到的名片
       :return:
       """
    action_str = input("请选择要执行的操作:"
                       "[1]/修改 [2]/删除 [0]/返回上一级")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱:")

        print("修改成功！")

    elif action_str == "2":
        card_list.remove(find_dict)

        print("删除成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典原有的值
    :param tip_message: 输入的提示信息
    :return: 如果用户输入信息返回内容（tip_message）没输入返回字典原有的值（dict-value）
    """

    # 1.提示用户输入
    result_str = input(tip_message)
    # 2.如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return  result_str

    # 3.用户没有输入返回字典中原有的值
    else:
        return dict_value
