file = open('romeo.txt')

list =[]
for line in file:
    uline = line.split()
    list.append(uline)
print(list)


while True:
    newdata = input('Enter your word')
    if newdata == 'Done':
        break
    elif newdata in list:
        continue
    else:
        list.append(newdata)
        print(list)
print('End of the program')
