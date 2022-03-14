#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    d = {}
    result = []
    freq = defaultdict(int)
    for i in range(len(queries)):
        op = queries[i][0]
        val = queries[i][1]
        
        occur = d.get(val,0)
        
        if op == 3:
            result.append(1 if freq.get(val) else 0)
        else:
            freq[occur] -= 1
            if op == 1:
                d[val] = occur + 1
            elif op == 2 and occur:
                d[val] -= 1
            freq[d.get(val,0)] += 1 
        
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
