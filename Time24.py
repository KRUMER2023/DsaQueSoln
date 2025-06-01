#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    n=len(s)
    if s[n-2:]=="AM":
        if s[:2]=="12":
            ti=ti="00"+s[2:n-2]
            return ti
        return s.replace("AM","")
            
    else:
        hr=s[:2]
        if int(hr)<12:
            hrs=12+int(hr)
            ti=str(hrs)+s[2:n-2]
            return ti
        return s.replace("PM","")
print(timeConversion("12:18:42AM"))
