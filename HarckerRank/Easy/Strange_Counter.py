#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

# def strangeCounter(t):
#     # Write your code here
#     initial_time=3
#     time=initial_time
#     for i in range(2,t+1):
#         if time==1:
#            initial_time=2*initial_time
#            time=initial_time
#         else:
#             time-=1
        
#     return time 

def strangeCounter(t):
    rem = 3
    while t > rem:
        t -= rem
        rem *= 2
    return rem - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
