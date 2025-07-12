import sys

import os
import serial
import pandas
import time
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

os.system('taskkill /f /im EXCEL.EXE')
ser = serial.Serial('COM7', baudrate=115200, timeout=2000)
binDataToExcel = {'inputToDAC': [], 'OINs': [], 'Arduino': []}
# intDataToExcel = {'inputToDAC': [], 'OINs': [], 'Arduino': []}
intDataToExcel = {'OINs': [], 'Arduino': []}

intDataToExcel['OINs'].append('OINs')
intDataToExcel['Arduino'].append('Arduino')
intDataToExcel['OINs'].append('OINs')
intDataToExcel['Arduino'].append('Arduino')

time.sleep(2)
print('Port is ready\nSet voltage:\n\tv<x> - maximum voltage (1<x<5)\n'
      '\t<x> - step of voltage (0<x<255)')
start = 12
# ser.write(start.to_bytes(1, sys.byteorder))
while 1:
    # maxV = 5
    # text = input()
    # mode = 0
    # if text[0] == 'v':
    #     mode = 1
    # step = int(text)
    # if step < 0:
    #     step = 0
    # elif step > 255:
    #     step = 255
    #
    # if mode == 1:
    #     maxV = step
    # else:
    #     ser.write(step.to_bytes(1, sys.byteorder))
    # time.sleep(0.5)
    # data = 0
    # while data == 0:
    #     data = ser.readline()
    data = ser.readline()
    print(data)
    a = data.decode('cp1251')
    print(a)
    startNum = a.find('я')
    endNum = a.find('\n')
    a = a[startNum + 1:len(a) - 2]
    print(a)
    # voltage = int(a[8:16], 2) * maxV / 255
    # print('voltage = {}', voltage)
    j = 0
    if len(a) > 0:
        for key in binDataToExcel:
            binDataToExcel[key].append(a[j * 8:(j + 1) * 8])
            j += 1
        j = 0
        b = a[len(a)-16:len(a)]
        for key in intDataToExcel:
            # print(a[j * 8:(j + 1) * 8])
            # if (j == 0):
            #     intDataToExcel[key].append(0)
            # else:
            #
            intDataToExcel[key].append(int(b[j * 8:(j + 1) * 8], 2))
            j += 1
        if a.find('11111111') == 0:
            break

bdf = pandas.DataFrame(binDataToExcel)
idf = pandas.DataFrame(intDataToExcel)

wb = Workbook()
ws = wb.active

for row in pandas.DataFrame(idf).itertuples(index=False):
    ws.append(row)
chart = LineChart()
# chart.x_axis('time')
# chart.y_axis('bits')
dataRef = Reference(ws, min_col=1,
                 min_row=2,
                 max_col=2,
                 max_row=len(idf)+1)
categoriesRef = Reference(ws, min_col=1,
                 min_row=2,
                 max_row=len(idf)+1)
chart.add_data(dataRef, titles_from_data=True)
chart.set_categories(categoriesRef)
ws.add_chart(chart,"D2")
wb.save('./intData.xlsx')

bdf.to_excel('./binData.xlsx')
# idf.to_excel('./intData.xlsx')
ser.close()
os.startfile('intData.xlsx')
