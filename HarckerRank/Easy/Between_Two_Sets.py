#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0
    # The number must be >= max(a) and <= min(b)
    start = max(a)
    end = min(b)
    
    for x in range(start, end + 1):
        # Condition 1: All elements in 'a' are factors of x
        cond1 = all(x % i == 0 for i in a)
        # Condition 2: x is a factor of all elements in 'b'
        cond2 = all(j % x == 0 for j in b)
        
        if cond1 and cond2:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
