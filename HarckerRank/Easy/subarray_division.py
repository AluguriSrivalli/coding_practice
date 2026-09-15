#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Approach: To solve this problem we have to find all the subarrays of given length(m) and whose elements sum turns out to be equal to provided value(d)
    # total no.of subarray can be determined by n(n+1)/2. But will result in duplicate pair incase of same values.
    # sum of the subarray : d (date)
    # length of subarray: m (month)
    # good approach is to go with sliding window
    n = len(s) 
    if n < m or m <= 0:   #edge case 
        return 0
    
    unique_subarrays = set()
    current_window_sum = sum(s[:m])
    
    if current_window_sum == d:
        unique_subarrays.add(tuple(s[:m]))
    
    for i in range(m, n):
        # Add the next element entering the window, subtract the one leaving it
        current_window_sum += s[i] - s[i - m]
        
        # If the sum matches, extract the subarray and add it to the set
        if current_window_sum == d:
            start_index = i - m + 1
            subarray = s[start_index : i + 1]
            unique_subarrays.add(tuple(subarray))
            
    return len(unique_subarrays)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
