with open('romeo.txt','r') as file:
    list =file.read().split()
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
