import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
# 通过json模块处理数据
f_us=open(r"C:\Users\26705\Desktop\IDE\py黑马\资料\可视化案例数据\折线图数据\美国.txt","r",encoding="utf-8")
us_data=f_us.read()
f_us.close()  # 关闭文件

# 去除不符合json规范的开头
us_data=us_data.replace("jsonp_1629344292311_69436(","")
# 去除不合规范的结尾
us_data=us_data[:-2]
# 转换为python数据
us_dict=json.loads(us_data)
print(type(us_dict))
print(us_dict)

# 获取trend key
trend_data=us_dict["data"][0]["trend"]
print(trend_data)
print(type(trend_data))

# 获取日期数据，用于x轴，取2020年
x_data=trend_data['updateDate'][:314]
print(x_data)

# 获取确认数据，用于y轴
y_data=trend_data['list'][0]['data'][:314]


# 生产图表
line=Line()
line.add_xaxis(x_data)
line.add_yaxis("2020年",y_data)
line.render()

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美国确诊人数",pos_left="center",pos_bottom="1%")
)
line.render()