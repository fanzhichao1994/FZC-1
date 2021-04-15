from pyecharts import charts, options
from pyecharts.commons.utils import JsCode
import pandas as pd
from pyecharts.globals import ChartType



data = pd.read_excel('国内疫情数据.xlsx')
map1 = charts.Map(init_opts=options.InitOpts(width='1200px', height='800px'))
map1.add('累计',         data_pair=[(x[1]['地区'], x[1]['累计']) for x in data.iterrows()],         maptype='china',         is_selected=True,         is_roam=True,         aspect_scale=0.75,         selected_mode='multiple',         label_opts=options.LabelOpts(is_show=True,                                      formatter=JsCode('''function(params){                                        if (params['value']){return params['name'] + ':' + params['value']}                                        else{return ''}                                        }''')),         is_map_symbol_show=False         )


map1.set_global_opts(
    visualmap_opts=options.VisualMapOpts(
            type_='color',
                  is_show=True,
                  pos_bottom='50%',
                  pos_left='0%',
                  min_=min(data['累计']),
                  max_=max(data['累计']),
                  is_piecewise=True,
                  pieces=[
                      {'min': min(data['累计']), 'max': 200},
                      {'min': 201, 'max': 300},
                      {'min': 301, 'max': 400},
                      {'min': 401, 'max': 500},
                      {'min': 501, 'max': 600},
                      {'min': 601, 'max': 700},
                      {'min': 701, 'max': 800},
                      {'min': 801, 'max': 900},
                      {'min': 901, 'max': 1000},
                      {'min': 1000, 'max': 10000},
                      {'value': 68151, 'label': '湖北', 'color': 'red'},
                      {'value': 10884, 'label': '香港', 'color': 'red'}
                  ]))
map2 = charts.Map3D(init_opts=options.InitOpts(width='1200px', height='800px'))
location = [('121.509062', '25.044332', '台湾'),
            ('114.502461', '38.045474', '河北'),
            ('112.549248', '37.857014', '山西'),
            ('111.670801', '40.818311', '内蒙古'),
            ('123.429096', '41.796767', '辽宁'),
            ('125.3245', '43.886841', '吉林'),
            ('126.642464', '45.756967', '黑龙江'),
            ('118.767413', '32.041544', '江苏'),
            ('120.153576', '30.287459', '浙江'),
            ('117.283042', '31.86119', '安徽'),
            ('119.306239', '26.075302', '福建'),
            ('115.892151', '28.676493', '江西'),
            ('117.000923', '36.675807', '山东'),
            ('113.665412', '34.757975', '河南'),
            ('114.298572', '30.584355', '湖北'),
            ('112.982279', '28.19409', '湖南'),
            ('113.280637', '23.125178', '广东'),
            ('108.320004', '22.82402', '广西'),
            ('110.33119', '20.031971', '海南'),
            ('104.065735', '30.659462', '四川'),
            ('106.713478', '26.578343', '贵州'),
            ('102.712251', '25.040609', '云南'),
            ('91.132212', '29.660361', '西藏'),
            ('108.948024', '34.263161', '陕西'),
            ('103.823557', '36.058039', '甘肃'),
            ('101.778916', '36.623178', '青海'),
            ('106.278179', '38.46637', '宁夏'),
            ('87.617733', '43.792818', '新疆'),
            ('116.405285', '39.904989', '北京'),
            ('117.190182', '39.125596', '天津'),
            ('121.472644', '31.231706', '上海'),
            ('106.504962', '29.533155', '重庆'),
            ('114.173355', '22.320048', '香港'),
            ('113.54909', '22.198951', '澳门')]
location_dict = {x[-1]: [x[0], x[1]] for x in location}
map2.add_schema(
    itemstyle_opts=options.ItemStyleOpts(
        color="rgb(5,101,123)",
        opacity=1,
        border_width=0.8,
        border_color="rgb(62,215,213)",
    ),
    map3d_label=options.Map3DLabelOpts(
        is_show=False,
        formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
    ),
    emphasis_label_opts=options.LabelOpts(
        is_show=False,
        color="#fff",
        font_size=10,
        background_color="rgba(0,23,11,0)",
    ),
    light_opts=options.Map3DLightOpts(
        main_color="#fff",
        main_intensity=1.2,
        main_shadow_quality="high",
        is_main_shadow=False,
        main_beta=10,
        ambient_intensity=0.3,
    ),
).add(
    series_name="bar3D",
    data_pair=[(x[1]['地区'], (location_dict[x[1]['地区']][0], location_dict[x[1]['地区']][1], x[1]['现有'])) for x in
               data.iterrows()],
    type_=ChartType.BAR3D,
    maptype='china',
    bar_size=1,
    shading="lambert",
    label_opts=options.LabelOpts(
        is_show=False,
        formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
    ),
).set_global_opts(title_opts=options.TitleOpts(title="Map3D-Bar3D"))

page = charts.Page()
page.add(map1).add(map2)
page.render('map.html')