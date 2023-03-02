
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:57:33 2023

@author: rainy
"""

import pandas as pd
from bokeh.io import output_file
# para visualizar el resultado
from bokeh.plotting import figure, show, gridplot
#from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool


df = pd.read_excel(
    'database.xlsx', header=1)
df = df.sort_values("FECHA")

output_file('page.html',
            title='GRÁFICA')

gk = df.groupby(["VARIABLE"])

data = gk.get_group("LLUVIA")
temp=gk.get_group("TMAX")
temau=temp['LA AURORA']


############## PLOTEANDO DATOS ###############################
#source = ColumnDataSource(data=dict(x=fechas,y=precip2018))

TOOLS = "save,pan,box_zoom,reset,wheel_zoom"
fig2 = figure(x_axis_type='datetime', title='',
             plot_height=200, plot_width=900, toolbar_location='below',
             y_axis_label="Precipitación (mm)", y_range=(-10, 150), background_fill_color='white', background_fill_alpha=0.6, tools=TOOLS)
line = fig2.line(data['FECHA'], data['SUIZA CONTENTA'],
                line_color="deepskyblue", line_width=1, legend_label='SUIZA CONTENTA')
#line = fig2.line(fechas, temp2018, line_color="red", line_width=1, legend_label='Temperatura C')
circle = fig2.circle(data['FECHA'], data['SUIZA CONTENTA'],
                    fill_color="blue", line_color="blue", size=2)
fig2.add_tools(HoverTool(tooltips=[
              ("Fecha", "@x{%d-%m-%Y}"), ("Precipitación", "@y{y.f} mm")], formatters={'@x': 'datetime', 'y': 'printf'}))
fig2.legend.location = 'top_left'
fig2.title.text_font_size = '15pt'
fig2.yaxis.axis_label_text_font_size = "15pt"

p = gridplot([[fig2]])

show(p)
