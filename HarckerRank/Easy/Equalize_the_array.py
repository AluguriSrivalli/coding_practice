#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):  
    # Write your code here
    n=len(arr) #8
    wordcount = {}
    for i in range(n): 
        num=arr[i]   
        if num in wordcount:
            wordcount[num]+=1 
        else:
            wordcount[num]=1 
    return n-max(list(wordcount.values()))
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
