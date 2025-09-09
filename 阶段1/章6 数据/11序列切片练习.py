# 有字符串万过月薪 员序程黑马 nohtyP学
# 用学过的任何方式，得到黑马程序员
str="万过月薪 员序程黑马 nohtyP学"

# 倒序整体，切片取出
str2=str[::-1][8:14]
print(str2)

# 先切片，然后再反转

str3=str[5:10][::-1]
print(str3)

# split分隔 空格 然后倒序字符串
str4=str.split(" ")
print(str4)
str5=str4[1][::-1]
print(str5)