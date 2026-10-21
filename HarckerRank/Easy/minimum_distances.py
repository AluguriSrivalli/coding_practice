#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    count_dict = defaultdict(list)

    for index, val in enumerate(a):
        count_dict[val].append(index)

    diff = []

    for indices in count_dict.values():
        if len(indices) > 1:
            for i in range(1, len(indices)):
                diff.append(indices[i] - indices[i - 1])

    return min(diff) if diff else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
