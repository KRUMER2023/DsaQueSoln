# import math

# def find_a_b(year):
#     n = int(year)
#     root = int(math.isqrt(n))  # Get the integer square root of n
    
#     if root * root != n:  # Check if n is a perfect square
#         return -1
    
#     # Now we need to find a and b such that a + b = root
#     for a in range(root + 1):
#         b = root - a
#         if b >= 0:
#             return (a, b)
    
#     return -1

# # Read number of test cases
# t = int(input())
# results = []

# for _ in range(t):
#     year = input().strip()
#     result = find_a_b(year)
#     if result == -1:
#         results.append("-1")
#     else:
#         results.append(f"{result[0]} {result[1]}")

# # Print all results
# print("\n".join(results))

import math

def isValid(s):
    n=int(s)
    r=int(math.isqrt(n))
    
    if r*r!=n:
        return -1
        
    for i in range(r+1):
        j=r-i
        if j>=0:
            return (i,j)
    return -1
    
t=int(input())
for _ in range(t):
    s=input()
    res=isValid(s)
    if res==-1:
        print(-1)
    else:
        print(res[0],res[1])