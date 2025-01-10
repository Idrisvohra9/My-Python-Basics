import math
import os
import random
import re
import sys

def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

s.lower()  # Yes, Python 3 has the lower() method for strings
s.islower()  # Yes, Python 3 has the islower() method for strings