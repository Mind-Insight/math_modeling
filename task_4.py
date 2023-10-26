num = int(input())
a, b = 1, 1
for _ in range(2, num + 1):
    print(a, end=" ")
    a, b = b, a + b
print(b)
