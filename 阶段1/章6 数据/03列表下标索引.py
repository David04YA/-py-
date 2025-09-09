#从0开始，嵌套列表也支持下标索引
name_list = [['张三','李四','王五'],['赵六','钱七','孙八']]
print(name_list[0][1]) #李四
print(name_list[1][2]) #孙八

#倒序取出

print(name_list[-1][-2]) #钱七  
print(name_list[-2][-1]) #王五