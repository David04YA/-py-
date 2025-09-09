# 新增/更新元素 字典[]=value 
# # 新增元素时如果key不存在，会新增
# # 新增元素时如果key存在，会覆盖


dict1={"name":"张三","age":18}
dict1["name2"]="李四"
dict1["age"]=19
print(dict1)

# 删除元素 del 字典[key] 字典.pop(key)

del dict1["name2"]
print(dict1)

dict1.pop("age")
print(dict1)

# 清空元素 dict.clear()
dict1.clear()
print(dict1)

# 获取全部的key 字典.keys()

dict2={"name":"张三","age":18}

keys=dict2.keys()
print(keys) 


# 遍历字典

# 方式1:通过获取到全部的key来完成遍历
for key in dict2.keys():
    print(key)
    print(dict2[key]) #字典的value

# 方式2:直接对字典进行for循环,每次循环都直接得到Key
for key in dict2:
    print(key)
    print(dict2[key]) #字典的value

# 字典不支持下标索引,所以不能while循环

# len统计数量
num=len(dict2)