from pyecharts import Funnel
import pandas as pd
import numpy as np
funnel = Funnel("漏斗图", width=600, height=400, title_pos='center')
funnel.add("商品交易行为记录数据", ['浏览', '加入购物车', '下单', '支付', '交易成功'], [40000, 18000, 10000, 8500, 8000], is_label_show=True,
           label_formatter='{b} {c}', label_pos="outside", legend_orient='vertical', legend_pos='left')
funnel.render()
funnel = Funnel("整体转化率", "图中的比例表示该行为下的用户数占总用户数（6万）的比例", width=600, height=400, title_pos='center')

funnel.add("商品交易行为记录数据", ['浏览', '加入购物车', '下单', '支付', '交易成功'],
           [int(100 * i / 60000) for i in [40000, 18000, 10000, 8500, 8000]], is_label_show=True,
           label_formatter='{b} {c}%', label_pos="outside",

           legend_orient='vertical', legend_pos='left')
funnel.render('data.html')
