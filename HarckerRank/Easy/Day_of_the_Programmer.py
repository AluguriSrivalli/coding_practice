#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Scenario-1
    if year == 1918:
        return f"26.09.{year}"
    
    # Scenario-2
    elif year >= 1700 and year <= 1917:
        if year % 4 == 0:
            return f"12.09.{year}"  # Leap year
        else:
            return f"13.09.{year}"  # Non-leap year
            
    # Scenario-3:
    elif year >= 1919 and year <= 2700:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"  # Leap year
        else:
            return f"13.09.{year}" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
