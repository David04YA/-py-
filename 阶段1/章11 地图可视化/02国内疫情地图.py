# 演示疫情可视化地图开发

import json
from pyecharts.charts import *
from pyecharts.options import TitleOpts, VisualMapOpts, LegendOpts
# 读取数据文件  
# 读取数据文件

f = open(r"C:\Users\26705\Desktop\IDE\py黑马\资料\可视化案例数据\地图数据\疫情.txt","r",encoding="utf-8")
data = f.read()

f.close()

# 将字符串json转换为python字典
data_dict=json.loads(data)

# 从字典中取出省份的数据

province_data_list=data_dict["areaTree"][0]["children"]

# 组装每个省份和确定人数为元祖，并将各个省的数据都封装进列表内

data_list=[] 
# 绘图需要用的数据列表
for province_data in province_data_list:
    province_name=province_data["name"]
    province_confirm=province_data["total"]["confirm"]
    data_list.append((province_name,province_confirm))

# 创建地图对象
map=Map()
# 添加数据
map.add("各省份确诊人数",data_list,"china")

# 设置全局配置项
map.set_global_opts(
    title_opts=TitleOpts(title="中国地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{
            "min":1,
            "max":99,
            "label":"1-99人",
            "color":"#CCFFFF"
        }]
    ),
    legend_opts=LegendOpts(is_show=False)
)

map.render()