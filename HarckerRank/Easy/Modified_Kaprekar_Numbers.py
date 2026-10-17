#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    result = []

    for i in range(p, q + 1):
        square = str(i * i)
        d = len(str(i))

        left = square[:-d]
        right = square[-d:]

        left_num = int(left) if left else 0
        right_num = int(right)

        if left_num + right_num == i:
            result.append(str(i))

    if result:
        print(" ".join(result))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
