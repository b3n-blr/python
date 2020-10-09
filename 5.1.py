line = input('Введите текст: ')
with open('5.1.txt', 'w') as my_f:
    my_f.writelines(line)
my_f = open('5.1.txt', 'w')
while line:
    my_f.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break
with open('5.1.txt', 'r') as my_f:
    print(my_f.readline())