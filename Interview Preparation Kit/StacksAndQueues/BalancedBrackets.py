#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def isBalanced(s):
    # Write your code here
    closeBrackets = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    stack = []
    if len(s) % 2 != 0:
        return "NO"
    for ch in s:
        if ch in closeBrackets:
            stack.append(ch)

        elif stack:
            if ch == closeBrackets[stack[-1]]:
                stack.pop()
            else:
                return "NO"
        else:
            return "NO"
    return "YES" if stack == [] else "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
