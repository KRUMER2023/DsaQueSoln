# You are given a string word.

# Return the maximum number of non-intersecting substrings of word that are at least four characters long and start and end with the same letter.

# A substring is a contiguous non-empty sequence of characters within a string.

res = []

def subS(s):
    ans = []
    n = len(s)
    used = [False] * n 

    for i in range(n):
        for j in range(i + 3, n):  
            if s[i] == s[j]:
                if not any(used[k] for k in range(i, j + 1)):
                    ans.append(s[i:j + 1])
                    for k in range(i, j + 1):
                        used[k] = True  
    return ans

s = "aabececbbeccdcdcbbdece"
res = subS(s)
print(res)

    