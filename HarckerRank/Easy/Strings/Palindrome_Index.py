#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    n=len(s)
    s_reverse=s[::-1]
    if s==s_reverse:
        return -1
    else:
        for i in range(n//2):
            if s[i]==s[-(i+1)]:
                pass
            else:
                s_new=s[:i]+s[i+1:]
                s_new_reverse=s_new[::-1]
                if s_new == s_new_reverse:
                    return i
                else:
                    return n-(i+1)
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
