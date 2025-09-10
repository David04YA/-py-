# 构建一个基础折线图
from pyecharts.charts import Line

from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts
# 得到折线图对象
line=Line()

# 添加x轴数据
line.add_xaxis(["中国","美国","日本"])


# 添加y轴数据
line.add_yaxis("2020年",[100,200,300])

# 设置全局配置项 set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="折线图",pos_left="center",pos_bottom="1%")
,
legend_opts=LegendOpts(is_show=True),
toolbox_opts=ToolboxOpts(is_show=True)

)
# 通过render方法，把代码生成为图像
line.render()


# pyecharts模块中有许多配置选项，常用
# 全局配置选项 系列配置选项

