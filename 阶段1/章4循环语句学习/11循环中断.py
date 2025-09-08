#continue 遇见continue跳过本次循环，继续下一次循环
#break 遇见break跳出整个循环
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")

# continue的嵌套
for i in range(1,6):
    print("外层循环语句1")
    for j in range(1,6):
        print("内层循环语句1")
        continue
        print("内层循环语句2")
    print("外层循环语句2")


for i in range(1,9999999):
    print("语句1")
    break
    print("语句2") 
print("循环结束")

for i  in range(1,6):
    print("外层循环语句1")
    for j in range(1,6):
        print("内层循环语句1")
        break
        print("内层循环语句2")
    print("外层循环语句2")