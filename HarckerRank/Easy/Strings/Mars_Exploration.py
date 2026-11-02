#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    changes = 0

    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2:
            expected = 'S'
        else:
            expected = 'O'

        if s[i] != expected:
            changes += 1

    return changes        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
