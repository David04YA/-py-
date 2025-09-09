# 字典：映射 就是key-value键值对
# 定义：{key:value,key:value,key:value}

# 空字典 dict1={} dict1=dict{}

dict1={"name":"张三","age":18} 
# 定义字典

dict2=dict()
# 定义空字典

# 定义重复Key的字典

dict3={"name":"张三","score":18,"score":90}
print(dict3)
# 字典不允许key重复,新的会覆盖旧的

# 基于key获取value
name=dict1["name"]
print(name)
age=dict1["age"]
print(age)
# 基于key获取value时如果key不存在会报错

# 基于get方法获取value
name=dict1.get("name")
print(name)
age=dict1.get("age")
print(age)
# 基于get方法获取value时如果key不存在不会报错，会返回None

# 字典的key和value也不限制数据类型,所以字典dict也能嵌套

# 例子:需求如下:记录学生各个科目考试信息
# 王力宏 语文77数学66英语55
# 周杰伦 语文88 英语55 数学99

dict_practice={"王力宏":{"语文":77,"数学":66,"英语":55},
              "周杰伦":{"语文":88,"数学":99,"英语":55}}
print(dict_practice)

# 总结,为什么使用字典:字典可以提供基于Key检索value的场景实现

# 字典特点:容纳多个数据 容纳不同类型的数据  每一份数据都是键值对