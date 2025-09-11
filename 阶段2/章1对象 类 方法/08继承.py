# 单继承
# 语法 class 类名(父类名):
#     类内容体

class test:
    IMEI=None
    producer="HH"

    def call_by_4g(self):
        print("正在通话中") 

class phone2(test):
    face_id="ON"

phone=phone2()
phone.call_by_4g()

# 多继承 py中一个类可以继承多个父类

class NFC:
    nfc_type="A"

    def read_card(self):
        print("正在读卡中")
        print("读卡")


class phone3(phone2,NFC):
    pass


p3=phone3()
p3.read_card()


