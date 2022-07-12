file = open('romeo.txt')


for line in file:
    uline = line.strip()
    fline = uline.strip('\n')
    zline = fline.split()
    print(zline)


for word in zline:
    newdata = input('Enter your word')
    if newdata is 'Done':
        break
    elif newdata is word:
        continue
    else:
        zline.append(newdata)
        print(zline)
print('End of the program')
