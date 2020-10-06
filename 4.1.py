from sys import argv
time, rate, bonus = argv[1:]
time = (float(time))
rate = (float(rate))
bonus = (float(bonus))
calc = time * rate + bonus
print('z', calc)
