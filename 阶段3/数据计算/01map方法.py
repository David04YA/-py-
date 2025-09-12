# map算子 将RDD数据一条条处理 返回新的RDD

from pyspark import SparkConf,SparkContext
import os
# 使用系统默认Python，避免路径问题
os.environ['PYSPARK_PYTHON']="python"
os.environ['PYSPARK_DRIVER_PYTHON']="python"
os.environ['PYARROW_IGNORE_TIMEZONE']='1'

conf = SparkConf().setMaster(
    "local[*]"
).setAppName(
    "test_app"
)
sc=SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5,6,7,8,9])

# 通过map方法将全部数据x10
def func(data):
  return data * 10

# 匿名函数
rdd2 = rdd.map(lambda x:x*10)
print(rdd2.collect())
#(T) -> U uD
# T: 输入类型
# U: 输出类型 代表返回值