#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = str(number)
last_d = last_d[-1]
comp = int(last_d)
if number < 0:
    comp = -1 * comp
if comp > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif comp == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
