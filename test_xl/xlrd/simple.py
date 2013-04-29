from xlrd import *

wb = open_workbook('example.xls')
for s in wb.sheets():
    print 'Sheet:', s.name
    for row in xrange(s.nrows):
        content = []
        for col in xrange(s.ncols):
            content.append(s.cell(row, col).value)
        print content
    print