# x轴上每一个点就是一个图表对象
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *

bar1=Bar()

bar1.add_xaxis(['A','B','C','D','E'])
bar1.add_yaxis('商家A',[1,2,3,4,5])
bar1.render()

bar2=Bar()
bar2.add_xaxis(['A','B','C','D','E'])
bar2.add_yaxis('商家A',[5,4,3,2,1])
bar2.render()

bar3=Bar()
bar3.add_xaxis(['A','B','C','D','E'])
bar3.add_yaxis('商家A',[5,4,3,2,1])
bar3.render()


# 构建时间线对象
timeline=Timeline()

# 在时间线内添加柱状图对象

timeline.add(bar1,'1月1日')
timeline.add(bar2,'1月2日')
timeline.add(bar3,'1月3日')

# 时间线绘图


# 自动播放
timeline.add_schema(play_interval=1000,
                     is_timeline_show=True,
                     is_auto_play=True,
                     is_loop_play=True)

timeline.render("时间线柱状图.html")