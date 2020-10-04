def script():
    time = float(input('выработка в часах: '))
    rate = float(input('ставка в час: '))
    bonus = float(input('размер премии: '))
    return time * rate + bonus
print(f'зарплата = {script()}')