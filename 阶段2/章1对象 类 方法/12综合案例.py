# 使用面向对象的思想

# 读取数据 封装数据对象 计算数据对象 pyecharts绘图

# 设计filereader类 设计数据封装类 对对象进行逻辑计算 

# 1.设计类实现数据封装

import json

class Record:
    def __init__(self,date,order_id,money,province):
        self.date=date #订单日期
        self.order_id=order_id #ID
        self.money=money #金额
        self.province=province #省份
    def __str__(self):
       return f"{self.date},{self.order_id},{self.money},{self.province}"

# 2设计抽象类，实现文件读取的功能，并用子类实现具体功能
class file_reader:
    def read_file(self) -> list[Record]:
        pass

class txt_reader(file_reader):
    def __init__(self,file_path):
        self.file_path=file_path  
        # 记录成员变量记录文件的路径
    # 实现抽象方法
    def read_data(self) -> list[Record]:
     f=  open(self.file_path,"r",encoding="utf-8")
     record_list:list[Record]=[]
     for line in f.readlines():
        line = line.strip()
        data_list=line.split(",")
        record =  Record(data_list[0],data_list[1],data_list[2],data_list[3])
        record_list.append(record)
     f.close()
     return record_list

class JsonFlieReader(file_reader):
    def __init__(self,file_path):
        self.file_path=file_path  

    def read_data(self) -> list[Record]:
     f=  open(self.file_path,"r",encoding="utf-8")
     record_list:list[Record]=[]
     for line in f.readlines():
       data_dict=json.loads(line) 
       record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
       record_list.append(record)

     f.close()
     return record_list

if __name__ == '__main__':
   text_file_reader=txt_reader(r"C:\Users\26705\Desktop\IDE\py黑马\资料\第13章资料\2011年1月销售数据.txt")
   json_file_reader=JsonFlieReader(r"C:\Users\26705\Desktop\IDE\py黑马\资料\第13章资料\2011年2月销售数据JSON.txt")
list1=text_file_reader.read_data()
list2=json_file_reader.read_data()
for l in list1:
    print(l)

for l in list2:
    print(l)