dictionary = {}
dictionary = {'addition' : '+', 'Subtraction' : '-', 'Multiplication' : '*', 'Division': '/'}

print(dictionary)
print(dictionary['addition'])

# del dictionary['Division'] #Удаление элемента

for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))