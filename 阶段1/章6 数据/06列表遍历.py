#如何遍历列表的元素
# 循环遍历
# 思考：循环条件如何控制？
def test1():
    list = [1,2,3,4,5]
   #循环控制变量用下标索引来控制，默认0
   #每次循环将下标加1
   #循环结束条件：下标索引变量<列表元素数量 

    index=0 #初始值为0
    while index<len(list):
     print(list[index])
     index+=1

test1()


#for循环来做 for循环更适合遍历
list=[1,2,3,4,5]
for i in list:
    print(i)


#while可以自定义循环条件 for只能从数据容器中取出元素
#for循环的循环次数是固定的  while循环的循环次数是不固定的