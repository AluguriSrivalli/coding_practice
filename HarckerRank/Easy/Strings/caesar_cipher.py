#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    capital_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k%=26
    new=""
    for letter in s:
        if letter in alpha:
            current_index=alpha.index(letter)
            new += alpha[(current_index + k) % 26]
        elif letter in capital_alpha:
            current_index=capital_alpha.index(letter)
            new += capital_alpha[(current_index + k) % 26]
        else:
            new+=letter
            
    return new
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
