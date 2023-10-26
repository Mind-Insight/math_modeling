b1, q, n = map(int, input().split())
print(*[b1 * q ** (i - 1) for i in range(1, n + 1)], sep="\n")
