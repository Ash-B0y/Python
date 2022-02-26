Student = [["jerry","65"], ["bob","1"], ["jerry","23"],["jerry","23"], ["jerry","100"],["Eric","83"]]
avg_dict = {}
for i in Student:
    if i[0] in avg_dict.keys():
        avg_dict[i[0]] = avg_dict[i[0]]+int(i[1])
    else:
        avg_dict[i[0]] = int(i[1])
print(max(avg_dict))

