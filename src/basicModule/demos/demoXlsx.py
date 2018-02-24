import xdrlib
import sys
import xlrd
import xlwt


# open a excel file.
def open_excel(file='input.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print("handle the exception.")


# open a excel file by sheet name.
def excel_table_byname(file='input.xlsx', colnameindex=0, by_name=u'Item'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    lists = []  # contain the data which store in excel.
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        if row:
            app = []
            for i in range(len(colnames)):
                app.append(row[i])
            lists.append(app)
    return lists


def excel_table_byindex(file='input.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    print("[excel_table_byindex] book & table: {}, {}".format(data, table))
    nrows = table.nrows
    ncols = table.ncols
    print("[excel_table_byindex] row & column: {}, {}".format(nrows, ncols))

    colnames = table.row_values(colnameindex)
    lists = []
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        if row:
            app = []
            for i in range(len(colnames)):
                app.append(row[i])
            # if app[0] == app[1]:
            #    lists.append(app)
    testXlwt('output.xls', lists)
    return lists


# write data to a new file.
def testXlwt(file='output.xls', lists=[]):
    print("[testXlwt] length of list:".format(len(lists)))
    book = xlwt.Workbook()  # create a excel
    sheet1 = book.add_sheet('sheet')  # create a sheet named 'sheet'

    i = 0
    for line in lists:
        j = 0
        for x in line:
            sheet1.write(i, j, x)
            j = j + 1
        i = i + 1

    book.save(file)


def testrw(file='output.xls'):
    book = xlwt.Workbook()
    table = book.add_sheet('test sheet')
    table.write(1, 0, 'the tested data')
    print("book & table: {}, {}".format(book, table))
    book.save(file)


def main():
    # testXlwt()
    # testrw()
    #''' read data by sheet index.
    tables = excel_table_byindex()
    for row in tables:
        print(row)  # '''

    ''' read data by sheet name.
    tables = excel_table_byname()
    for row in tables:
        print(row)  # '''


if __name__ == "__main__":
    main()
    pass
