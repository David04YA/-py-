# 获取Mysql数据库连接对象
from pymysql import Connection  
conn=Connection(
    host="localhost", #主机名或IP地址
    port=3306,#端口 默认3306
    user="root",#账户名
    password="123456",#密码
    database="world"
)

cursor=conn.cursor()

# cursor.execute("INSERT INTO city(name,countrycode,district,population) VALUES('北京','CHN','北京',1000000)")
# 在执行数据插入或其他更改数据的sql语句时，需要用代码确认更改行为
# 连接对象.commit（）

cursor.execute("INSERT INTO city(ID,Name,CountryCode,District,Population) VALUES('北京','CHN','北京',1000000)")
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()