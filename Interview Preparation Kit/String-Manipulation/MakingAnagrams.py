#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    count = 0
    da = {}
    db = {}
    for i in a:
        if i not in da:
            da[i] = 1
        else:
            da[i] += 1
    for i in b:
        if i not in db:
            db[i] = 1
        else:
            db[i] += 1
            
    for i in set(da).union(set(db)):
        count += abs(da.get(i,0)-db.get(i,0))
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
