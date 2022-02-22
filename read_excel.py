# install xlrd using 'pip install xlrd'

import xlrd

path = ('')  # path of excel file
workbook = xlrd.open_workbook(path)

# get the sheet by name
sheet = workbook.sheet_by_name('Orders')
# get number of rows
print('Total number of rows:', sheet.nrows)
# get number of columns
print('Total number of columns:', sheet.ncols)
# get particular cell value
print('Particular cell value:', sheet.cell_value(0, 0))
# get all rows and columns
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(sheet.cell_value(row, col), end=" | ")
    print('')
