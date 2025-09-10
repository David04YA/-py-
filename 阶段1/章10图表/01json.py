# 带有特定格式的字符串，作为一种数据交换格式

# python数据和json数据的转换

# 导入json
import json

# 准备符合json格式的python数据

data = {"name":"张三","age":18}

# 通过json.dumps(data)方法把python数据转化为json数据

data=json.dumps(data,ensure_ascii=False)
print(type(data))
print(data)
# 通过json.loads(data)把json数据转化为py数据
data=json.loads(data)
print(type(data))
print(data)