# 掌握构建一个基础的柱状图并能够反转xy轴

from pyecharts.charts import Bar

bar=Bar()

bar.add_xaxis(['A','B','C','D','E'])
bar.add_yaxis('商家A',[1,2,3,4,5])
bar.render()
