# 1. 系统随机生成一个随机数
#import random
# random_number = random. randint ( a: 1, b: 100)
# 2. 用户根据提示猜数字，并将所猜的数字输入系统
# 3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4.如果猜对，系统自动退出，游戏结束



import random
random_num = random.randint(1,100)

while True:
    num = int(input("请输入您猜的数字:"))
    if num > random_num:
        print("您猜的数字太大了")
        continue
    elif num < random_num:
        print("您猜的数字太小了")
        continue
    else:
        print("恭喜您,猜对了666!")
        break