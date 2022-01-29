#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

#method 1
"""
def checkMagazine(magazine, note):
    # Write your code here
    for word in note:
        try:
            magazine.remove(word)
        except:
            print("No")
            return
    print("Yes")

"""

#method 2
def checkMagazine(magazine,note):
    d = {}
    for word in magazine:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    for word in note:
        if word in d and d[word]>0:
            d[word] -= 1
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
