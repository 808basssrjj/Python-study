has_ticket = True
knife_length = 30

if has_ticket:
    print("车片检查通过，准备安检")

    if knife_length > 20:
        print("你带的刀太长，有%dcm长" % knife_length)
        print("不允许上车")
    else:
        print("安检通过")
else:
    print("请先买票")
