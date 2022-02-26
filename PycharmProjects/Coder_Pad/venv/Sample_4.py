lst = [23, 2, 3, 12, 2, 2, 34, 55, 66, 79]
lth =len(lst)
i=0
while i<lth:
     if lst[i]==2:
         lst.insert(i+1,2)
         i+=1
         del lst[lth]
     i+=1
print(lst)