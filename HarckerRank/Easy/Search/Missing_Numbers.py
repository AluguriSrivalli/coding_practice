#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter,defaultdict
#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    arr_count=Counter(arr)
    brr_count=Counter(brr)
    final=[]
    for val in brr_count:
        if arr_count[val]!=brr_count[val]:
            final.append(val)
    final=final

    return sorted(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
