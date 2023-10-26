a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Треугольник равнобедренный")
    elif a != b != c:
        print("Треугольник разносторонний")
    else:
        print("Треугольник равносторонний")
else:
    print("Такого треугольника не существует")
