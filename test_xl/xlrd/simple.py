from xlrd import *
import os

cur_path = os.path.join(os.path.dirname(__file__), '..')
up_path = os.path.realpath(cur_path)
get_path = lambda x:os.path.join(up_path, x)
print get_path('xlrd/')
ab_path = get_path('xlrd/') + 'Book1.xlsx'
print ab_path
wb = open_workbook(ab_path)
for s in wb.sheets():
    print 'Sheet:', s.name
    for row in xrange(s.nrows):
        content = []
        for col in xrange(s.ncols):
            content.append(s.cell(row, col).value)
        print content
    print