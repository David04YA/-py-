# 为什么捕获异常：程序运行过程中回出现bug
# # 遇到bug时两种情况：1.整个程序停止运行 2.对Bug进行提醒，继续允许

# 基本语法：
# try:
#     # 可能会出现异常的代码
# except:
#     # 处理异常的代码

try:
    f=open("bill.txt","r",encoding="utf-8")
except:
    print("文件不存在")

# 捕获指定异常

try:
    f=open("bill.txt","r",encoding="utf-8")
except FileNotFoundError as e:
    print("出现了文件不存在的异常")

# 捕获多个异常
# 捕获多个异常时，需要使用元组的方式进行捕获，放在except后
try:
    f=open("bill.txt","r",encoding="utf-8")
except (FileNotFoundError,UnicodeDecodeError) as e:
    print("出现了文件不存在或编码错误的异常")
 
 # 捕获所有异常
try:
    f=open("bill.txt","r",encoding="utf-8")
except Exception as e:
    print("出现了未知异常")

# 异常的else和finally
# else：如果没有异常发生，会执行else中的代码
# finally：无论是否发生异常，都会执行finally中的代码
try:
    f=open("bill.txt","r",encoding="utf-8")
except Exception as e:
    print("出现了未知异常")
else:
    print("没有异常发生")
finally:
    print("无论是否发生异常，都会执行")