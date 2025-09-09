#列表是可以修改的，元祖是不可以修改的 希望封装数据，又不希望数据被篡改，就用元祖

#元祖定义

#用小括号，用逗号隔开，数据可以是不同的数据类型 

#定义空元祖 变量名称=() 变量名称=tuple()

t2=(1,"hello",True)
t1 =()
t3=tuple()

print(type(t1))
print(type(t3))

#定义单个元祖，元素后面要加逗号
t4=(1,)
print(t4)
print(type(t4))

# 元祖也支持嵌套
t5 = (1,2,3,("a","b","c"))
print(t5)
print(t5[3])
print(t5[3][1])


#元祖操作，因为不可修改所以少了一些方法
#元祖的方法：count() index() len()

index=t5[3].index("a")
print(index)

count=t5[3].count("a")
print(count)
t5_len=len(t5)
print(t5_len)

#元祖遍历
i=0
while i<t5_len:
    print(t5[i])
    i=i+1

for i in t5:
    print(i)

#不可修改元祖中的内容，否则直接报错，但嵌套元祖中的内容可以修改