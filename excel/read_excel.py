# @Author ZhangGJ
# @Date 2021/07/02 14:09

import xlrd


def read_excel():
    wb = xlrd.open_workbook('文思老数据台账编号（需刷新到ADD表）.xls')
    sheet = wb.sheet_by_name('Sheet1')
    for a in range(sheet.nrows):
        cells = sheet.row_values(a)
        stt = cells[1]
        sttt = '\'' + stt + '\','
        with open('test.txt', 'a') as f:
            f.write(sttt)


if __name__ == '__main__':
    read_excel()
