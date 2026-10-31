#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    missing_types = 0
    if not any(char.isdigit() for char in password):
        missing_types += 1
    if not any(char.islower() for char in password):
        missing_types += 1
    if not any(char.isupper() for char in password):
        missing_types += 1
    special_characters = "!@#$%^&*()-+"
    if not any(char in special_characters for char in password):
        missing_types += 1
        
    missing_length = 6 - n
    return max(missing_types, missing_length)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
