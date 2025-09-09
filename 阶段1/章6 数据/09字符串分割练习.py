#给定一个字符串 1.统计有多少it字符 2.将字符内的所有空格替换成| 3.按照|分割

strtest="itheima and itcast"

num=strtest.count("it")
print(num)

newstr=strtest.replace(" ","|")
print(newstr)

newstr2=newstr.split("|")
print(newstr2)