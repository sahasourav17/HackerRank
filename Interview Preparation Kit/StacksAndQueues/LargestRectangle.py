#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(heights):
    maxArea, stack = 0, []
    for i, h in enumerate(heights):
        startIdx = i
        while stack and stack[-1][1] > h:
            idx,height = stack.pop()
            maxArea = max(maxArea,(i-idx)*height)
            startIdx = idx
        stack.append((startIdx,h))
    # print(stack)
    for i,h in stack:
        maxArea = max(maxArea, h*(len(heights)-i))
    return maxArea

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()