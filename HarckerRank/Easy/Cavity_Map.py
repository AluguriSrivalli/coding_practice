#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    grid=[list(row) for row in grid]
    for i in range(1,n-1):
        for j in range(1,n-1):
            if grid[i-1][j]<grid[i][j] and grid[i+1][j]<grid[i][j] and grid[i][j+1]<grid[i][j] and grid[i][j-1]<grid[i][j]:
                grid[i][j]='X'
                
            else: 
                pass
                
    return ["".join(row) for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
