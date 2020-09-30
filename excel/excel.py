import xlsxwriter

from db.DB import DB

db = DB()
tests = db.getAllTestResults()
# создаём документ
workbook = xlsxwriter.Workbook('example.xlsx', {'remove_timezone': True})
# создаём вкладку в документе
worksheet = workbook.add_worksheet()
# форматирование
cellPass = workbook.add_format(dict(font_color='green', bold=True))
cellFail = workbook.add_format(dict(font_color='red', bold=True))
date_format = workbook.add_format(dict(num_format='d mmm yyyy hh:mm:ss'))
worksheet.set_column('B:B', 45)
worksheet.set_column('E:E', 20)

# названия столбцов
worksheet.write('A1', '№')
worksheet.write('B1', 'Название')
worksheet.write('C1', 'Успех')
worksheet.write('D1', 'Фиаско')
worksheet.write('E1', 'Дата')

# значения
for i, test in enumerate(tests):
    worksheet.write('A' + str(i + 2), i + 1)
    worksheet.write('B' + str(i + 2), test['name'])
    if test['result']:
        worksheet.write('C' + str(i + 2), 1, cellPass)
    else:
        worksheet.write('D' + str(i + 2), 1, cellFail)
    worksheet.write('E' + str(i + 2), test['date_time'], date_format)

# подсчёт сумм
worksheet.write('F1', 'Успешные')
worksheet.write('G1', 'Не Успешные')
worksheet.write('F2', '=SUM(C:C)', cellPass)
worksheet.write('G2', '=SUM(D:D)', cellFail)

# рисуем графики
# chart = workbook.add_chart(dict(type='column'))
# chart.add_series(dict(values='=Sheet1!$F2'))
# chart.add_series(dict(values='=Sheet1!$G2'))
# worksheet.insert_chart('H7', chart)
chart = workbook.add_chart(dict(type='doughnut'))

chart.add_series({
    'name': 'Результаты тестов',
    'categories': '=Sheet1!$F$1:$G$1',
    'values':     '=Sheet1!$F$2:$G$2',
    'data_labels': {'percentage': True},
    'points': [
        {'fill': {'color': 'green'}},
        {'fill': {'color': 'red'}},
    ],
})
# Set a 3D style.
chart.set_style(26)

worksheet.insert_chart('H7', chart)


workbook.close()
