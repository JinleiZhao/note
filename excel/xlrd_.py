import xlrd  #读单元格
import xlwt  #写单元格
import os

path = os.path.dirname("__file__")
print("path",path)
#打开表格：
book = xlrd.open_workbook('./file.xlsx') #encoding_override='utf_8'
#获取所有工作簿
sheet_names_list = book.sheet_names()
print(sheet_names_list)
#获取某个工作簿
sheet = book.sheet_by_index(1) #根据索引
sheet = book.sheet_by_name('Sheet1') #根据名字
print (sheet)

print(sheet.name) #名称
print(sheet.nrows) #总行数
print(sheet.ncols) #总列数

for i in range(2, sheet.nrows, 3):
    print('i',i)

rows = sheet.row_values(3)#根据索引获取某行的所有数据
print(rows)
cols = sheet.col_values(3)#根据索引获取某列的所有数据
print(cols)

#获取单元格内容：
print(sheet.cell(1,0).value) #现获取单元格对象，在获取数据
print(sheet.cell_value(1,1)) #直接获取数据
print(sheet.row(1)[3].value)

#获取单元格数据种类
print(sheet.cell(1,3).ctype) #0--empty, 1--string, 2--number(浮点)， 3--date, 4--boolean, 5--error


