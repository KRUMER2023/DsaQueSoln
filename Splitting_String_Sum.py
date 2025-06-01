# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
s="00111"
Max=float("-inf")
n=int(s,2)
one=0
while(n>0):
    n=n&(n-1)
    one+=1
l=len(s)
zero=0

for i in range(l):
    if s[i]=='0':
        zero+=1
    print(one , zero)
    Max=max(Max,one+zero)
print(Max)

    