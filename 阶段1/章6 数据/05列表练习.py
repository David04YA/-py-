#1.定义列表，用变量接收它
list = [1,2,3,4,5]

#2.追加一个数字31到列表尾部
list.append(31)
print(list) #[1, 2, 3, 4, 5, 31]


#3.追加一个列表到列表尾部
list.extend([6,7,8])
print(list) #[1, 2, 3, 4, 5, 31, 6, 7, 8]

# 4.取出第一个元素
num1=list[0]
print(num1) #1

#5.取出最后一个元素
num2=list[-1]
print(num2) #8

#6查询元素31

# 列表.index(元素) 找不到报错ValueError
print(list.index(31)) #5



