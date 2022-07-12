file = open('romeo.txt')


for line in file:
    uline = line.strip()
    fline = uline.strip('\n')
    list = fline.split()
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
