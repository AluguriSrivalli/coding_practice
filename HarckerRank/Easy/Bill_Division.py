#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

# This problem emphasizes the importance of preserving decimal values. If `total` and `index_value` are stored as integers, the calculation may produce incorrect results when either value is odd. Therefore, they should be handled as decimal values to ensure accurate division.

def bonAppetit(bill, k, b):
    # Write your code here
    total = sum(bill)/2
    index_value = (bill[k]/2)
    final = total - index_value
    
    if final == b:
        print("Bon Appetit")
    else:
        print(int(index_value))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
