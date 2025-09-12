# Pyspark针对数据的处理，都以RDD对象为载体
# 数据都存储在RDD内，各类数据的计算方法也是RDD的成员方法，返回的也是RDD对象
# PySpark支持通过SpearkContext对象的parallelize方法将Python对象转换为RDD对象
# 包括 List tuple set dict str

# rdd = sc.parallelize(数据容器对象）

from pyspark import SparkContext,SparkConf

conf = SparkConf().setMaster(
    "local[*]"
).setAppName(
"test_app"
)

sc=SparkContext(conf=conf)

rdd=sc.parallelize([1,2,3,4,5,6,7,8,9])

# 如果要查看RDD内的内容，要用collect方法
print(rdd.collect())


rdd = sc.textFile(r"C:\Users\26705\Desktop\IDE\py黑马\hello.txt")
print(rdd.collect())
sc.stop()