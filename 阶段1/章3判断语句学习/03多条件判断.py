# if elif else
print("多条件判断")
test1=int(input("请输入一个数字:"))
if test1>0:
    print("这个数字是正数")
elif test1<0:
    print("这个数字是负数")
else:
    print("这个数字是0")

height=int(input("请输入你的身高:"))
level=int(input("请输入你的等级:"))
if height>=180 and level>=5:
    print("你可以参加选拔")
elif height>=180 and level<5:
    print("你可以参加选拔")
else:
    print("你不可以参加选拔")

# 判断是互斥且有序的，即符合第一个条件后，后续条件不再判断。