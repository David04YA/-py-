#发工资案例 编号1-20员工，每人1000
#判断员工绩效分（1-10） 若<5,不发工资下一位
# 钱没了就直接不发，共1W本金
# continue用于跳过员工，break用于结束发工资



money=10000
for i in range(1,21):
  import random
  score=random.randint(1,10)
  if score<5:
    print(f"员工{i}绩效分{score}，不发工资")
    continue
  if money<1000:
    print("钱没了，不能发了")
    break
  money-=1000
  print(f"员工{i}绩效分{score}，发工资1000，还剩{money}")