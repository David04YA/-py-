# 集合：不支持重复元素（自带去重）,内容无序
# 集合定义 {元素,元素,元素}

# 定义空集合 set1=set()

# 集合是无序的，所以集合不支持下标索引访问
# 集合是可变的，所以集合支持添加和删除元素

my_set={1,2,3,4,5,6,7,8,9}
my_set.add(10)
print(my_set)
my_set.remove(10)
print(my_set)

# 随机取出元素 集合.pop() 同时集合中这个元素会被移除
my_set.pop()
print(my_set)
# 列表中也能Pop，可以指定下标，集合不能

# clear
my_set.clear()
print(my_set)

# 取两个集合间的差集，得到新集合，集合1和2不变
set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,4,5,6,7,8,9,10}
set3=set1-set2
print(set3) 

# 消除两个集合的交集 集合1.difference_update(集合2) 集合1会被改变，集合2不变
set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,4,5,6,7,8,9,10}
set1.difference_update(set2)
print(set1)
print(set2)

# 集合合并 集合1.union(集合2) 集合1和2不变
set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,4,5,6,7,8,9,10}
set3=set1.union(set2)
print(set3)
print(set1)
print(set2)

# 统计len
print(len(set3))

# 集合的遍历，集合不支持下标索引所以不能while
for i in set3:
    print(i)
