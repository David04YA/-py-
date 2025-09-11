# 创建到mysql数据库连接

from pymysql import Connection

# 获取Mysql数据库连接对象
conn=Connection(
    host="localhost", #主机名或IP地址
    port=3306,#端口 默认3306
    user="root",#账户名
    password="123456",#密码
    database="world"
)

print(conn.get_server_info)
# 执行非查询性质sql

# 获取游标对象
cursor=conn.cursor()
conn.select_db("world")

# # 使用游标对象 执行sql语句
# cursor.execute("CREATE TABLE test_pymysql(id INT, info VARCHAR(20))")



# 执行查询性质的SQL语句
cursor.execute("SELECT * FROM city")
test = cursor.fetchall()

for r in  test:
    print(r)
# 关闭连接
conn.close()