try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误%s" % result)
else:
    print("尝试成功")
finally:
    print("无论有没有出现错误都会执行的代码")

print("-" * 50)
