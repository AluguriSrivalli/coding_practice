#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    unique_chars = set(s)
    max_length = 0
    
    # Generate all possible pairs of 2 unique characters
    for char1, char2 in combinations(unique_chars, 2):
        # Filter the string to keep only the current pair
        filtered = [c for c in s if c == char1 or c == char2]
        
        # Check if the filtered characters alternate
        is_valid = True
        for i in range(len(filtered) - 1):
            if filtered[i] == filtered[i+1]:
                is_valid = False
                break
                
        # If it is valid, update the maximum length found so far
        if is_valid:
            max_length = max(max_length, len(filtered))
            
    return max_length
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
