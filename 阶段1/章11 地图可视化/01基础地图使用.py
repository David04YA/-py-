# 演示地图基础使用

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map=Map()

data=[("北京市",99),("上海市",100),("广州市",101)]

# 添加数据
map.add("地图",data,"china")

map.render()

map.set_global_opts(
visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
        {"min":0,"max":50,"label":"0-50","color":"#CCFFFF"},
        {"min":50,"max":100,"label":"50-100","color":"#FFFF99"},
        {"min":100,"max":150,"label":"100-150","color":"#FF9966"},
        {"min":150,"max":200,"label":"150-200","color":"#FF6666"},
        {"min":200,"max":300,"label":"200-300","color":"#CC3333"},
        {"min":300,"label":"300+","color":"#990033"},
    ]
    ),
)


map.render()