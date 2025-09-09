# #列表功能 插入 删除 清除元素 统计元素个数 修改函数

# 在py中，如果将函数定义为class的成员，该函数会被称为方法

def add(a,b):
    return a+b
#函数 面向过程为函数

class Dog: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
#类 面向对象为方法


#使用格式不同

# 函数的使用
result = add(1,2)

# 方法的使用
dog=Dog('小白',1)


#查询功能 列表.index() 找不到报错ValueError
name_list = ['张三','李四','王五','张三']
print(name_list.index('张三')) #0
print(name_list.index('张三',1)) #从下标1开始找 张三


#修改功能 列表[下标]=新值
name_list[0] = '张三'
print(name_list) #['张三', '李四', '王五', '张三']

#插入功能 列表.insert(下标,元素)  列表.append(元素) 追加到末尾
name_list.insert(1,'赵六')
print(name_list) #['张三', '赵六', '李四', '王五', '张三']
name_list.append('王二')
print(name_list) #['张三', '赵六', '李四', '王五', '张三', '王二']


#删除功能 列表.remove(元素） del 列表.pop(下标) 
# 列表.pop(下标) 删除指定下标元素 并返回该元素
mlist = [1,2,3,4,5]
print(mlist.pop(2)) #3
print(mlist) #[1, 2, 4, 5]
test2 = [1,2,3,4,5,2,3,4,5]
test2.remove(2) #删除第一个2
print(test2) #[1, 3, 4, 5, 2, 3, 4, 5]

del test2[0] #删除下标为0的元素
print(test2) #[3, 4, 5, 2, 3, 4, 5]
#清除功能 列表.clear() 清空列表
test2.clear()

#统计功能 统计列表内某个元素出现的次数 列表.count(元素)
test3 = [1,2,3,4,5,2,3,4,5]
print(test3.count(2)) #2

#统计有多少元素 列表.__len__() 列表.length()
print(test3.__len__()) #9
print(test3.length()) #9  

# 列表有以下特点：
# 可以存储多个数据
# 数据类型可以不同
# 数据是有序的
# 允许数据重复
# 可以修改 可以嵌套