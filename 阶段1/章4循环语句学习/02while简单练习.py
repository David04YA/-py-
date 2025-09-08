# 需求：while来求1-100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
# 需求：while来求1-100的偶数和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)  
# 需求：while来求1-100的奇数和
i = 1
sum = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1
print(sum)  
# 需求：while来求1-100的能被3整除的数的和
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum += i
    i += 1
print(sum)  