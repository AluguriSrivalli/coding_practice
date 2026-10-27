#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s: str) -> str:
    stack = []
    
    for char in s:
        # If the stack has elements and the top element matches the current character,
        # we found an adjacent matching pair, so we pop it from the stack.
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Otherwise, push the character onto the stack.
            stack.append(char)
            
    # If the stack is empty, return "Empty String" as specified by the problem.
    if not stack:
        return "Empty String"
        
    # Reconstruct the final reduced string from the remaining characters.
    return "".join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
