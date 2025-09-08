#构建一个随机数字变量
import random
num=random.randint(1,10)

guess=int(input("请输入你猜想的数字:"))
if guess==num:
    print("恭喜你猜对了")
else:
    if guess > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
guess = int(input("请重新输入你猜想的数字:"))
if guess==num:
    print("恭喜你猜对了")
else:
    if guess > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
guess = int(input("请重新输入你猜想的数字:"))
if guess==num:
    print("恭喜你猜对了")
else:
    print(f"很遗憾，你没有猜对，正确数字是{num}")
    print("游戏结束")