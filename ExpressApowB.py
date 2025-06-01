import sys

def precompute_powers(limit):
    power_set = set()
    a = 2
    while a * a <= limit:
        p = a * a
        while p <= limit:
            power_set.add(p)
            p *= a
        a += 1
    return power_set

power_set = precompute_powers(10**8)

results = []
t=int(input())
for i in range(t):
    n = int(input())
    results.append("Yes" if n in power_set else "No")

print("\n".join(results))
