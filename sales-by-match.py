#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_count = {}
    for sock in ar:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1

    pairs = 0
    for count in color_count.values():
        pairs += count // 2
    
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
