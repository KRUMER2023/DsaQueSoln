def max_chocolate_kept(n, m, k):
    total = n * m
    max_keep = 0

    if k == 0:
        return total

    for i in range(1, n):
        part1 = i * m
        part2 = (n - i) * m
        if part1 >= k:
            max_keep = max(max_keep, part2)
        if part2 >= k:
            max_keep = max(max_keep, part1)

    for j in range(1, m):
        part1 = n * j
        part2 = n * (m - j)
        if part1 >= k:
            max_keep = max(max_keep, part2)
        if part2 >= k:
            max_keep = max(max_keep, part1)

    return max_keep
    
t= int(input())
n,m,k=map(int,input().split())
print(max_chocolate_kept(n,m,k))