while True:
    try:
        n = int(input("Введите n: "))
        if n >= 1:
            break
        else:
            print("n должно быть положительным числом")
    except ValueError:
        print("Введите целое число")

s = 0
for i in range(1, n + 1):
    s += i

print(f"Сумма чисел от 1 до {n} = {s}")
