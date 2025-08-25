#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(a, b, k):
    
     
    count = 0
    for i in range(a, b + 1):   # inclusive range
        reversed_num = int(str(i)[::-1])   # reverse the current number
        if abs(i - reversed_num) % k == 0:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(a, b, k)

    fptr.write(str(result) + '\n')

    fptr.close()
