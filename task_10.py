num = int(input())
i = 2
while i * i <= num:
    if num % i != 0:
        i += 1
    else:
        num //= i
        print(i, end=" ")
if num != 1:
    print(num)
