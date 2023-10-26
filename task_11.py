def find_num_divisors_sum(n):
    res = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            res += i
            d = n // i
            if d != i:
                res += d
        i += 1
    return res


num = int(input())
print(*[i for i in range(2, num + 1) if i == find_num_divisors_sum(i)])
