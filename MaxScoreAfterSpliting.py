# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

def maxScore( s):
    """
    :type s: str
    :rtype: int
    """
    n=len(s)
    Max=float("-inf")
    for i in range(n):
        if i==n-1:
            break
        zero=s[:i+1].count('0')
        one=s[i+1:].count('1')
        Max=max(Max,one+zero)
    return Max
    
print(maxScore("011101"))