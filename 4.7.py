from itertools import count
from math import factorial

def gen():
    for el in count(1):
        yield factorial(el)

gen1 = gen()
x = 0
for i in gen1:
    if x < 15:
        print(i)
        x += 1
    else:
        break