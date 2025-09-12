# 构建Psypark执行环境入口对象
# PySpark的执行环境入口对象是类SparkContext的类对象

from pyspark import SparkContext,SparkConf

# 创建SparkConf类对象

conf=SparkConf().setMaster(
    "local[*]"
).setAppName(
    "test_app"
)

# 基于SparkConf类对象创建SparkContext类对象
sc=SparkContext(conf=conf)

print(sc.version)

sc.stop()

# Pyspark的编程：数据输入得到RDD 通过RDD类对象的成员方法
# 完成需求
# 将处理后的RDD对象写出文件，转换成List等

