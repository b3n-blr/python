with open('5.5.txt', 'w') as f:
    num = input('Введите цифры через пробел: ')
    f.writelines(num)
    num2 = num.split()

    print(sum(map(int, num2)))