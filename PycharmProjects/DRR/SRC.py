import xlrd
import csv
import xlsxwriter
DPU_AND_PORT = []
DPU_AND_PORT_sl = []
LOC = []
LOC_sl = []
Columns = []
Info = []
Index = []
Flag = 0
Discrepancies = []
output = ''
idx = 0
f = open("C:/Users/Ash/Desktop/@$h/Input.txt", "r")
for x in f:
    s = x.split("=")
    Info.append(s[1])

if '\n' not in Info and not len(Info) == 0:

    wb = xlrd.open_workbook(Info[2][0:len(Info[2])-1])
    sheet = wb.sheet_by_name('Data Cut-In Summary')
    sh = wb.sheet_by_index(0)
    cell = sheet.cell(0, 0)

    for rv in range(0, 1):
        Columns.append(sheet.row(rv))

    for i in range(0, len(Columns[0])):
        if len(Index) == 3:
            break
        if "DPU_ID" in Columns[0][i].value or "PORT_NAME" in Columns[0][i].value or "OBJECT_NAME" in Columns[0][i].value:
            Index.append(i)

    for i in range(sheet.nrows):
        if "LOC" in str((sheet.cell_value(i, Index[2]))):
            port_no = int(sheet.cell_value(i, Index[1]))
            DPU_AND_PORT.append(str((sheet.cell_value(i, Index[0])))+"-"+str(port_no))
            LOC.append(str((sheet.cell_value(i, Index[2]))))

    with open(Info[1][0:len(Info[1])-1], 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:
            if "DPU" in row[0] and "LOC" in row[1] and len(row[3]) == 1:
                DPU_AND_PORT_sl.append(row[0]+"-"+str(row[3]))
                LOC_sl.append(row[1])
    SAM = Info[0][0:1] + Info[0][1:4].upper() + Info[0][4:7]
    workbook = xlsxwriter.Workbook(Info[3]+'Validation_Summary.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    if SAM not in DPU_AND_PORT_sl[0] or SAM not in DPU_AND_PORT[0]:

        if SAM not in DPU_AND_PORT_sl[0]:
            output = 'Place the Authentic SL_TO_NE File in the mentioned Path.....'
        if SAM not in DPU_AND_PORT[0]:
            output = 'Place the Authentic DRR File in the mentioned Path.....'
        if SAM not in DPU_AND_PORT[0] and SAM not in DPU_AND_PORT_sl[0]:
            output = 'Place the Authentic DRR and SL_TO_NE File in the mentioned Path.....'
        Flag = 2
    else:
        for i in range(0, len(DPU_AND_PORT_sl)):
            if DPU_AND_PORT_sl[i] in DPU_AND_PORT:
                idx = DPU_AND_PORT.index(DPU_AND_PORT_sl[i])
                if not LOC_sl[i] == LOC[idx]:
                    Flag = 1
                    Discrepancies.append(LOC_sl[i])
            else:
                Discrepancies.append(LOC_sl[i])
                Flag = 1

    if Flag:
        if Flag == 1:
            output = 'The Following Location/s have DPU-Port Mapping Discrepancies...'
            worksheet.write(row, col, output)
            row += 1
            for i in Discrepancies:
                worksheet.write(row, col, i)
                row += 1
            workbook.close()
    else:
        output = 'DPU-Port Mapping Between T-18 and PNI are Authentic.....'
        worksheet.write(row, col, output)
        workbook.close()

    worksheet.write(row, col, output)
    workbook.close()

else:
    workbook = xlsxwriter.Workbook('Validation_Summary.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    output = 'Configuration File Corrupted.....'
    worksheet.write(row, col, output)
    workbook.close()
