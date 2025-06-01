#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(a,n):
    # Write your code here
    p,ne,z=0,0,0
    for i in a:
        if i == 0:
            z+=1
        elif i<0:
            ne+=1
        else:
            p+=1
    print(f"{p/n:.6f}")
    print(f"{ne/n:.6f}")
    print(f"{z/n:.6f}")
    
if __name__ == '__main__':


    plusMinus([-4, 3, -9, 0, 4, 1],n=6)
