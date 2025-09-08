i=1
for i in range(1,101):
    print("今天是我表白的第%d天" % i)
    for j in range(10):
        print(f"送你第{j+1}朵花")
    print("我送完了")
    i += 1
    print("第%d天表白结束" % (i-1))