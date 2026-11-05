#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)

    for i in range(1, (n // 2) + 1):
        first_num_str = s[:i]

        if first_num_str[0] == '0' and len(first_num_str) > 1:
            continue
            
        first_num = int(first_num_str)

        built_str = ""
        current_num = first_num
        
        while len(built_str) < n:
            built_str += str(current_num)
            current_num += 1

        if built_str == s:
            print(f"YES {first_num}")
            return

    print("NO")

              

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

