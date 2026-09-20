#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):

    frequency = {}
    for num in a:
        frequency[num] = frequency.get(num, 0) + 1
        
    max_length = 0
    
    for num in frequency:
        current_length = frequency[num] + frequency.get(num + 1, 0)
        max_length = max(max_length, current_length)
        
    return max_length
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
