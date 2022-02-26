s = "aaaaabccccgggaa"
o = ""
temp_ctr = 1
for i in range(0, len(s)):
    if i == len(s)-1:
        o += s[i] + str(temp_ctr)
    elif s[i+1] != s[i]:
        if temp_ctr == 1:
            o += s[i]
        else:
            o += s[i]+str(temp_ctr)
            temp_ctr = 1

    else:
        temp_ctr += 1
lst = list(map(str, o))
print(lst)