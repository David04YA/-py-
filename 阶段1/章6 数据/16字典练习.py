# 需求:通过for循环,对所有级别为1的员工,级别上升1级,薪水增加1000元

dict= {"张三":{"级别":1,"薪水":5000},
        "李四":{"级别":2,"薪水":8000},
        "王五":{"级别":1,"薪水":5000}}

for key in dict:
    if dict[key]["级别"]==1:
        dict[key]["级别"]+=1
        dict[key]["薪水"]+=1000
print(dict)

for name in dict:
    if dict[name]["级别"]==1:
        dict[name]["级别"]+=1
        dict[name]["薪水"]+=1000
print(dict)

