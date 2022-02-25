# install xlwt using: pip install xlwt

import xlwt

# create workbook
workbook = xlwt.Workbook()

# add sheet
sheet = workbook.add_sheet('Fruits')

# apply styles like font and font-color
title_style = xlwt.easyxf('font: bold 1, color red;')

# write to sheet
sheet.write(0, 0, 'Sr No.', title_style)
sheet.write(0, 1, 'Fruits', title_style)

sheet.write(1, 0, '1')
sheet.write(1, 1, 'Apple')
sheet.write(2, 0, '2')
sheet.write(2, 1, 'Banana')
sheet.write(3, 0, '3')
sheet.write(3, 1, 'Cherry')

# save excel
workbook.save('fruits.xls')
