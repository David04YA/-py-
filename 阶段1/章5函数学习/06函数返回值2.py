# 如果函数没有使用return，还是有返回值，返回nonetype字面量

def say_hello():
    print("hello")
    # return None  # 可以省略
result = say_hello()
print(result)  # None 接收到的返回值

def check(age):
     if age >= 18:
         return "成年人"
     else:
         return None
     
result = check(20)
if not result:
    print("未成年")
else:
    print("成年人") 