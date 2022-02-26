import xlrd

data_from_excel = []
wb = xlrd.open_workbook("C:/Users/Ash/Desktop/@$h/Excel_generated_by_dataextraction.xlsx")
sheet = wb.sheet_by_index(0)
cell = sheet.cell(0, 0)
for i in range(sheet.nrows):
    temp = []
    if not str((sheet.cell_value(i, 0))):
        continue
    temp.append(str((sheet.cell_value(i, 0))))
    temp.append(str((sheet.cell_value(i, 1))))
    temp.append(str((sheet.cell_value(i, 2))))
    data_from_excel.append(temp)

# 2nd column from excel sheet in sorted order without white space
in_cable_sorted = sorted([i for i in data_from_excel[1:] if i[1] != ""], key=lambda x: x[1])
print(in_cable_sorted)
list_of_splited_in_cable = [i[1].split(" ")[0] for i in in_cable_sorted]
for i in in_cable_sorted:
    second_value = i[1]
    third_value = i[2]
