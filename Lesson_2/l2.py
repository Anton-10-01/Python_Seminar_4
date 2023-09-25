list_1 = []

for i in range(5):
    list_1.append(i)
    print(list_1)
print(len(list_1))
print(list_1.pop()) #Удаление с конца списка
print(list_1)
print(list_1.pop(3)) #Удаление по индексу
print(list_1)
print(list_1.insert(1,11)) #Замена на втором индексе значание
print(list_1)