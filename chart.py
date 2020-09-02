from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

rows = [
    ('季度销售额', '电脑', '手机'),
    ('一季度', 23, 35),
    ('二季度', 24, 36),
    ('三季度', 25, 37),
    ('四季度', 26, 45)
]

wb = Workbook()
ws = wb.active

for row in rows:
    ws.append(row)

chart = BarChart()
chart.title = '季度产品销售额'
chart.y_axis.title = '销售额（万元）'
chart.x_axis.title = '季度'

data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=5)
titles = Reference(ws, min_col=1, min_row=2, max_row=5)

chart.add_data(data, titles_from_data=True)
chart.set_categories(titles)

ws.add_chart(chart)
wb.save('chart.xlsx')
