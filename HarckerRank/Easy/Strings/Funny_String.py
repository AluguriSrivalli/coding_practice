#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s_reverse=s[::-1]
    Ascii_differ_s=[]
    ascii_differ_s_reverse=[]
    # print(s_reverse)
    for i in range(len(s)-1):
        Ascii_differ_s.append(abs(ord(s[i+1])-ord(s[i])))
        ascii_differ_s_reverse.append(abs(ord(s_reverse[i+1])-ord(s_reverse[i])))
    
    Ascii_length=len(Ascii_differ_s)
    ordinal_value=[]
    reverse_ordinal_value=[]
    for j in range(Ascii_length-1):
        ordinal_value.append(abs(Ascii_differ_s[j+1]-Ascii_differ_s[j]))
        reverse_ordinal_value.append(abs(ascii_differ_s_reverse[j+1]-ascii_differ_s_reverse[j]))
        
    if ordinal_value==reverse_ordinal_value:
        return "Funny"
    else:
        return "Not Funny"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

