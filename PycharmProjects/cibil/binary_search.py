li = [21, 34, 55, 67, 87, 90, 92, 95]

iter = [0]

def binary_search(num, start, stop):
    iter[0] += 1
    if len(li[start:stop + 1]) <= 1:
        if li[0] != num:
            return "not in list"
        return li.index(num)
    mid = (start + stop) // 2
    if li[mid] == num:
        return li.index(num)
    elif li[mid] < 34:
        return binary_search(num, mid + 1, stop)

    else:
        return binary_search(num, start, mid)


print(binary_search(21, 0, len(li)))
print(iter)