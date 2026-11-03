#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    unique_s = set()
    for ch in s.lower():
        if ch.isalpha():
            unique_s.add(ch)

    if len(unique_s) == 26:
        return "pangram"
    else:
        return "not pangram"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
