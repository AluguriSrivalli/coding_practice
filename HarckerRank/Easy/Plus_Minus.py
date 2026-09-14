#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = [i for i in arr if i > 0]
    negative = [i for i in arr if i < 0]
    zero = [i for i in arr if i == 0]
    total = len(arr)
    
    print(f"{len(positive) / total:.6f}")
    print(f"{len(negative) / total:.6f}")
    print(f"{len(zero) / total:.6f}")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
