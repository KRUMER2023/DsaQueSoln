K = 20  # Safe due to fast growth of powers of 2

MOD = 998244353
MAXN = 100005
p2 = [1] * MAXN
for i in range(1, MAXN):
    p2[i] = (p2[i - 1] * 2) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    
    A = [p2[val] for val in p]
    B = [p2[val] for val in q]

    ans = [0] * n

    for i in range(min(K, n)):
        for j in range(min(K, n)):
            if i + j < n:
                ans[i + j] = max(ans[i + j], (A[i] + B[j]) % MOD)

    print(' '.join(map(str, ans)))
