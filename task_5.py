num1, num2 = map(int, input().split())
try:
    res = num1 / num2
    print("Первое число делится на второе")
    if num1 % num2:
        print(f"Остаток равен {num1 % num2}")
    print(f"Частное равно {res}")
except ZeroDivisionError as e:
    print(e)
