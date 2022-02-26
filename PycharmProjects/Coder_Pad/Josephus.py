idx = 1
n = 2
survival_counter = 0
l = list(range(1, 15))
sze = len(l)
while len(l) != 1:
    if survival_counter >= len(l):
        survival_counter = 0

    elif idx == n and survival_counter < len(l):
        del l[survival_counter]
        idx = 1
    else:
        idx += 1
        survival_counter += 1
print(l[0])
