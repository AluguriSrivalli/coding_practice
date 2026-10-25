#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
def happyLadybugs(b):
  has_empty = "_" in b

  if has_empty:
    counts = {}
    for char in b:
      if char != "_":
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
      if count == 1:
        return "NO"
    return "YES"
  else:
    # No empty cells: every ladybug must already be happy
    n = len(b)
    for i in range(n):
      current = b[i]
      left_match = i > 0 and b[i - 1] == current
      right_match = i < n - 1 and b[i + 1] == current
      if not left_match and not right_match:
        return "NO"
    return "YES"

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

