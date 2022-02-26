import xlrd
s1 = []
s2 = []
l1 = []
l2 = []
l3 = []
Trace = []
wb = xlrd.open_workbook("C:/Users/Ash/Desktop/@$h/Excel_generated_by_dataextraction.xlsx")
sheet = wb.sheet_by_index(0)
cell = sheet.cell(0,0)
for i in range(sheet.nrows):
    if not str((sheet.cell_value(i, 0))):
        continue
    l1.append(str((sheet.cell_value(i, 0))))
    l2.append(str((sheet.cell_value(i, 1))))
    l3.append(str((sheet.cell_value(i, 2))))

for j in range(1,len(l1)):
    #del Trace[:]
    s1=l1[j].split("-")
    a=int(s1[2])
    if not l2[j] or "X" in l2[j] or "X" in l3[j]:
        continue
    if "IN" in l3[j]:
        Trace.append(l1[j])
        Trace.append(l2[j])
        Trace.append(l3[j])
        s2 = l3[j].split()
        temp = s2[0]+" OUT1"
        temp1 = s2[0]+" OUT2"
        temp2 = l3[l2.index(temp)]
        temp3 = l3[l2.index(temp1)]
        Trace.append(l2[l2.index(temp)])
        Trace.append(l3[l2.index(temp)])
        Trace.append(l2[l2.index(temp1)])
        Trace.append(l3[l2.index(temp1)])
        if temp2 not in l2:
            for k in range(0,len(l2)):
                if te
        #Trace.append(l2[l2.index(temp2)])
        #Trace.append(l3[l2.index(temp2)])
print (Trace)
