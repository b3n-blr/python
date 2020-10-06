from itertools import count, cycle
for num in count(start=5):
    print(num)
    if num == 10:
        break


a = 0
for el in cycle(['a', 'b', 'c']):
    if a > 10:
        break
    print(el)
    a += 1