#做一个黑马ATM
#要求：每次执行函数后都返回主菜单 每次存款、取款后都显示当前余额



#定义全局变量money name
money = 5000000
name = None
#要求客户输入名
name = input("请输入您的姓名：")
#定义查询函数
def query(show_header):
    if show_header:
     print("---查询余额---")
     print("尊敬的%s,您的余额为%d元"%(name,money))
#定义存款函数
def saving(num):
    global money
    print("---存款---")
    money = money + num
    print("尊敬的%s,您成功存入%d元,当前余额为%d元"%(name,num,money))
#定义取款函数
def get_money(num):
    global money
    print("---取款---")
    money = money - num
    print("尊敬的%s,您成功取出%d元,当前余额为%d元"%(name,num,money))
#定义主菜单函数
def main():
    print("---主菜单---")
    print("1.\t查询余额")
    print("2.\t存款")
    print("3.\t取款")
    print("4.\t退出")
    return input("请输入您的选择：")
#设置无限循环，确保程序不退出
while True:
   Keyboard_input=main()
   if Keyboard_input == "1":
       query(True)
       continue  #跳过本次循环，继续下一次循环
   elif Keyboard_input == "2":
       saving(int(input("请输入存款金额：")))
       continue  #跳过本次循环，继续下一次循环
   elif Keyboard_input == "3":
       get_money(int(input("请输入取款金额：")))
       continue  #跳过本次循环，继续下一次循环
   elif Keyboard_input == "4":
       print("谢谢使用")
       break  #退出循环
