#string 字符串 int 整数 float 浮点型
print(type("hello")) #string
print(type(100))     #int
print(type(100.0))   #float

# 使用变量存储type()的结果
string_type = type("hello")
int_type = type(100)
float_type = type(100.0)

print(string_type)
print(int_type)
print(float_type)

test=type("hello")
print(test)  #变量无类型，它存储的数据有类型