list_1 = [1, 12, 3, 4, 5]
k = 11
min = abs(k-list_1[0])
s = 0

for i in range(1, len(list_1)):
    count = abs(k - list_1[i])
    if count < min:
        min = count
        s = i
print(list_1[s])