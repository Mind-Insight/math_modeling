a, b, c = map(int, input().split())
D = b**2 - 4 * a * c
if D == 0:
    print(-b / 2 * a)
elif D > 0:
    print((-b + D**0.5) / 2 * a, (-b - D**0.5) / 2 * a, sep="\n")
elif D < 0:
    print("Нет действительных корней")
