#SORTING SOCK WARMUP ON HACKERRANK
#8 minutes (required aid from stackoverflow) https://stackoverflow.com/questions/60200557/sock-merchant-problem-i-am-trying-to-do-this-with-a-different-approach
#basic logic - reduce socks to unique set, then compare each unique value to how many pairs there are. Increment a generalized counter.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    #we have an we sample from which is ar and a count of socks n
    totalPairs = 0
    #get unique values so we don't doublecount
    sockSet = set(ar)
    for i in sockSet:
        #we compare each number and add the number of pairs
        totalPairs += int(ar.count(i) / 2)
    return totalPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
